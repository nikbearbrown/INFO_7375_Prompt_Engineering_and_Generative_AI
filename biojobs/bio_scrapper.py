import requests
from bs4 import BeautifulSoup
import os
import time
import re
from urllib.parse import urljoin, urlparse
import random
import argparse

# List of common user agents to rotate
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
]

def get_headers(base_url):
    """Generate headers with a random user agent and other browser-like headers"""
    parsed_url = urlparse(base_url)
    referer = f"{parsed_url.scheme}://{parsed_url.netloc}/"
    
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': referer,
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

def clean_filename(url):
    # Extract the path part of the URL and convert to a valid filename
    path = urlparse(url).path
    # Remove leading and trailing slashes
    path = path.strip('/')
    # Replace remaining slashes with underscores
    path = path.replace('/', '_')
    # If path is empty (homepage), use "index"
    if not path:
        return "index.html"
    # Add .html extension if not present
    if not re.search(r'\.\w+$', path):
        path = path + '.html'
    # Limit filename length
    if len(path) > 200:
        path = path[:190] + path[-10:]
    return path

def extract_domain_name(url):
    """Extract just the domain name without protocol"""
    parsed_url = urlparse(url)
    return parsed_url.netloc

def get_domain_with_protocol(url):
    """Extract the full domain with protocol"""
    parsed_url = urlparse(url)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"

def get_links(url, base_domain):
    try:
        session = requests.Session()
        response = session.get(url, headers=get_headers(base_domain), timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        # Find all links that are within the same domain
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            full_url = urljoin(url, href)
            parsed_url = urlparse(full_url)
            
            # Skip fragment links (anchors to same page)
            if not parsed_url.path and parsed_url.fragment:
                continue
                
            # Skip non-HTTP protocols
            if not parsed_url.scheme.startswith('http'):
                continue
                
            # Only include links to the same domain
            if full_url.startswith(base_domain):
                # Normalize URL by removing fragments
                normalized_url = full_url.split('#')[0]
                links.append(normalized_url)
        
        return list(set(links))  # Remove duplicates
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def download_page(url, output_dir, base_domain):
    try:
        filename = clean_filename(url)
        filepath = os.path.join(output_dir, filename)
        
        # Skip if already downloaded
        if os.path.exists(filepath):
            print(f"Skipping {url} (already downloaded)")
            return filepath
        
        print(f"Downloading {url} to {filename}")
        session = requests.Session()
        response = session.get(url, headers=get_headers(base_domain), timeout=10)
        response.raise_for_status()
        
        # Save the HTML content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        # Add variable delay between requests to appear more human-like
        time.sleep(random.uniform(2, 5))
        
        return filepath
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def scrape_website(base_url, root_output_dir, max_pages=None):
    # Make sure base_url has a scheme
    if not base_url.startswith('http'):
        base_url = 'https://' + base_url
    
    # Get the domain from the base URL
    base_domain = get_domain_with_protocol(base_url)
    
    # Extract clean domain name for directory
    domain_name = extract_domain_name(base_url)
    
    # Create domain-specific output directory
    output_dir = os.path.join(root_output_dir, domain_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Start with the homepage
    to_visit = [base_url]
    visited = set()
    
    # Keep track of all downloaded files
    downloaded_files = []
    
    page_count = 0
    
    while to_visit and (max_pages is None or page_count < max_pages):
        current_url = to_visit.pop(0)
        
        if current_url in visited:
            continue
            
        visited.add(current_url)
        page_count += 1
        
        # Download the page
        filepath = download_page(current_url, output_dir, base_domain)
        if filepath:
            downloaded_files.append(filepath)
        
        # Find links on the page and add to queue
        links = get_links(current_url, base_domain)
        for link in links:
            if link not in visited and link not in to_visit:
                to_visit.append(link)
    
    return downloaded_files, domain_name, output_dir

def combine_files(files, output_dir, domain_name):
    combined_file = os.path.join(output_dir, f"{domain_name}_combined.html")
    print(f"Combining {len(files)} files into {combined_file}...")
    
    with open(combined_file, 'w', encoding='utf-8') as outfile:
        outfile.write(f"<html><head><title>{domain_name} Combined Content</title></head><body>\n")
        
        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    
                    # Extract the main content
                    soup = BeautifulSoup(content, 'html.parser')
                    
                    # Get relative file path for display
                    rel_path = os.path.basename(file)
                    
                    # Try to reconstruct original URL
                    original_url = rel_path.replace('_', '/').replace('.html', '')
                    if original_url == "index":
                        original_url = domain_name
                    else:
                        original_url = domain_name + "/" + original_url
                    
                    # Add source URL as comment and visible reference
                    outfile.write(f"<!-- Source: {original_url} -->\n")
                    
                    # Try different selectors based on the site structure
                    main_content = None
                    for selector in ['main', 'article', '.entry-content', '.content', '#content', 
                                    '#main-content', '.main-content', '.page-content']:
                        main_content = soup.select_one(selector)
                        if main_content:
                            break
                    
                    # If no specific content area found, use the body
                    if not main_content:
                        main_content = soup.body
                    
                    if main_content:
                        # Add a header with the page title
                        title = soup.title.string if soup.title else os.path.basename(file)
                        outfile.write(f"<h1>{title}</h1>\n")
                        outfile.write(f"<div class='source-url'><a href='https://{original_url}'>{original_url}</a></div>\n")
                        outfile.write(str(main_content))
                        outfile.write("<hr>\n")
                    else:
                        print(f"Could not extract main content from {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}")
        
        outfile.write("</body></html>")
    
    return combined_file

def main():
    parser = argparse.ArgumentParser(description='Web scraper for domains')
    parser.add_argument('--domain', type=str, default='avillach-lab.hms.harvard.edu',
                        help='Domain to scrape (default: avillach-lab.hms.harvard.edu)')
    parser.add_argument('--max-pages', type=int, default=100,
                        help='Maximum number of pages to scrape (default: 100)')
    parser.add_argument('--output-dir', type=str, default='scraped_sites',
                        help='Root output directory (default: scraped_sites)')
    
    args = parser.parse_args()
    
    # Normalize the domain by removing protocol if present
    domain = args.domain
    if domain.startswith('http://'):
        domain = domain[7:]
    elif domain.startswith('https://'):
        domain = domain[8:]
    
    # Create root output directory if it doesn't exist
    root_output_dir = args.output_dir
    if not os.path.exists(root_output_dir):
        os.makedirs(root_output_dir)
    
    print(f"Starting scrape of {domain}")
    print(f"Will download up to {args.max_pages} pages")
    print(f"Root output directory: {root_output_dir}")
    
    downloaded_files, domain_name, domain_output_dir = scrape_website(domain, root_output_dir, args.max_pages)
    
    if downloaded_files:
        combined_file = combine_files(downloaded_files, domain_output_dir, domain_name)
        print(f"Scraping complete. Downloaded {len(downloaded_files)} pages.")
        print(f"Combined content saved to {combined_file}")
    else:
        print("No files were downloaded.")

if __name__ == "__main__":
    main()