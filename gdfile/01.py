import gdown

def download_from_file(file_with_links):
    # Open the file containing the Google Drive links
    with open(file_with_links, 'r') as file:
        # Read each line (each Google Drive link)
        links = file.readlines()
    
    # Download each file from the Google Drive links
    for link in links:
        # Strip any surrounding whitespace/newlines
        link = link.strip()
        
        # Check if the link is non-empty
        if link:
            print(f"Downloading file from: {link}")
            try:
                # gdown.download will download the file to the current directory
                gdown.download(link, quiet=False, fuzzy=True)
                print(f"Downloaded file from {link}")
            except Exception as e:
                print(f"Failed to download from {link}. Error: {str(e)}")

if __name__ == "__main__":
    # Replace with the path to your file containing Google Drive links
    file_with_links = "demo121.txt"
    
    # Download files from the links in the file
    download_from_file(file_with_links)
