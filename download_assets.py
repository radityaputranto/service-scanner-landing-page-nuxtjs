import os
import re
import urllib.request
import json
from html.parser import HTMLParser

PAGES = {
    "home": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzRmMDZkNDI4ZTExOTQxNGY4YTViYTMwMzAyZTQ3ZmM0EgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086",
    "tips": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2E5MjM2ZTE5NTJiYjRkMGJhMTI5NGEwNzE0ZjQ2MDIzEgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086",
    "kontak": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzNhMWZmOGY3YzNhOTRlNzZiZTZhODQ5NWI4OTQ0YTM4EgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086",
    "layanan": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sXzYzMDVkMmFiNjNkMzRkMjliNzFkZjIyYmY3NjYxMmY0EgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086",
    "tentang": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2Y5NWI4MDY1Y2M3YTRkZjdhNTM0YTc0M2ZjM2Q3ZWJiEgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086",
    "portofolio": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2U2NWU4MGRhODdlZTQyYzU5NWQzNDYwZmIyZWI5ZTg3EgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086",
    "sparepart": "https://contribution.usercontent.google.com/download?c=CgthaWRhX2NvZGVmeBJ8Eh1hcHBfY29tcGFuaW9uX2dlbmVyYXRlZF9maWxlcxpbCiVodG1sX2NlNDUwMGQ1ZTA1NDQ1NDFhMTkzN2FmN2M1NGQzMzA5EgsSBxDhjbLs8hcYAZIBJAoKcHJvamVjdF9pZBIWQhQxNzUzODIxNTcyNTc3MTg0ODg0OQ&filename=&opi=89354086"
}

WORKSPACE = "/Users/user/project/personal/service-scanner-landing-page"
HTML_DIR = os.path.join(WORKSPACE, "stitch_html")
PUBLIC_DIR = os.path.join(WORKSPACE, "public", "images")

os.makedirs(HTML_DIR, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def clean_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-\.]', '_', name)

class ImageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            attrs_dict = dict(attrs)
            src = attrs_dict.get('src')
            if src:
                alt = attrs_dict.get('alt', '')
                data_alt = attrs_dict.get('data-alt', '')
                self.images.append({
                    'src': src,
                    'alt': alt,
                    'data_alt': data_alt
                })

images_to_download = []

for page_name, url in PAGES.items():
    print(f"Fetching {page_name} page HTML...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        
        # Save HTML locally for backup
        html_file = os.path.join(HTML_DIR, f"{page_name}.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Saved HTML to {html_file}")
        
        # Find images in HTML using built-in parser
        parser = ImageParser()
        parser.feed(html)
        
        for idx, img in enumerate(parser.images):
            src = img['src']
            alt = img['alt']
            data_alt = img['data_alt']
            
            # Determine category based on alt text, src, page name
            category = "general"
            alt_lower = (alt + " " + data_alt).lower()
            
            if "logo" in alt_lower or "client" in alt_lower or "partner" in alt_lower:
                category = "logos"
            elif "hero" in alt_lower or "banner" in alt_lower or "maintenance" in alt_lower:
                category = "hero"
            elif "technician" in alt_lower or "repair" in alt_lower or "servis" in alt_lower or "workshop" in alt_lower:
                category = "services"
            elif "spare" in alt_lower or "part" in alt_lower or "roller" in alt_lower or "adf" in alt_lower:
                category = "spareparts"
            elif "testi" in alt_lower or "avatar" in alt_lower or "andi" in alt_lower or "bapak" in alt_lower:
                category = "testimonials"
            elif "tips" in alt_lower or "blog" in alt_lower or "tutorial" in alt_lower or "edukasi" in alt_lower:
                category = "blog"
            elif page_name == "tentang" or "tentang" in alt_lower or "about" in alt_lower:
                category = "about"
            elif page_name == "sparepart":
                category = "spareparts"
            elif page_name == "layanan":
                category = "services"
            elif page_name == "portofolio":
                category = "portfolio"
            elif page_name == "tips":
                category = "blog"
                
            # If still general
            if category == "general":
                if page_name == "home":
                    if "technician" in alt_lower or "working" in src:
                        category = "services"
                    else:
                        category = "hero"
            
            # Clean image name
            ext = ".png"
            if "jpg" in src or "jpeg" in src:
                ext = ".jpg"
            elif "svg" in src:
                ext = ".svg"
            elif "webp" in src:
                ext = ".webp"
                
            img_id = f"{page_name}_{idx}"
            if alt:
                img_id = clean_filename(alt.lower().replace(" ", "_"))
            
            filename = f"{img_id}{ext}"
            
            images_to_download.append({
                "src": src,
                "category": category,
                "filename": filename,
                "page": page_name
            })
            
    except Exception as e:
        print(f"Error fetching {page_name}: {e}")

print(f"Found {len(images_to_download)} images to download.")

# Download unique images
downloaded_urls = {}
for item in images_to_download:
    url = item["src"]
    if url in downloaded_urls:
        continue
    
    category = item["category"]
    filename = item["filename"]
    
    cat_dir = os.path.join(PUBLIC_DIR, category)
    os.makedirs(cat_dir, exist_ok=True)
    
    dest_path = os.path.join(cat_dir, filename)
    
    # Check if file already exists with same name, if so append count
    count = 1
    base, ext = os.path.splitext(filename)
    while os.path.exists(dest_path):
        filename = f"{base}_{count}{ext}"
        dest_path = os.path.join(cat_dir, filename)
        count += 1
        
    print(f"Downloading {url} to {dest_path}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            with open(dest_path, 'wb') as f:
                f.write(response.read())
        # Store clean public path for nuxt (e.g. /images/hero/hero.png)
        rel_path = f"/images/{category}/{filename}"
        downloaded_urls[url] = rel_path
        print(f"Successfully downloaded to {dest_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("Assets download summary:")
for url, path in downloaded_urls.items():
    print(f"- {url} -> {path}")

# Output mapping for replacement in frontend
mapping_path = os.path.join(WORKSPACE, "image_mapping.json")
with open(mapping_path, 'w', encoding='utf-8') as f:
    json.dump(downloaded_urls, f, indent=2)
print(f"Saved image mapping to {mapping_path}")
