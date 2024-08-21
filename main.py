import requests
from bs4 import BeautifulSoup
from utils.colors import BLUE, GREEN, RED
from utils.printer import Printer

def download_manga(url):
    # Get the html content of the page
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')
    # get id chapter-detail
    chapter_detail = soup.find(id='chapter-detail')
    
    if chapter_detail is None:
        raise Exception("Chapter not found")
    
    chapter_content = chapter_detail.get_text(separator="\n", strip=True)
    Printer.print_with_style(chapter_content, BLUE)

        
def get_manga_url():
    manga_url = input("Please enter manga URL (or 'q' to quit): ").strip()
    if not manga_url:
        Printer.print_with_style("Manga URL cannot be empty. Please try again.", RED)
        return get_manga_url()
    return manga_url

def get_chapter():
    chapter = input("Please enter chapter (or 'q' to change URL): ").strip()
    if not chapter.isdigit() and chapter != "q":
        Printer.print_with_style("Invalid chapter. Please enter a valid chapter number or 'q' to quit.", RED)
        return get_chapter()
    return chapter

def download_chapter(manga_url, chapter):
    url = f"{manga_url}/chuong-{chapter}"
    try:
        download_manga(url)
    except Exception as e:
        Printer.print_with_style(f"Failed to download chapter {chapter}. Error: {e}", RED)

def main():
    while True:
        manga_url = get_manga_url()
        if manga_url.lower() == "q":
            Printer.print_with_style("Goodbye", GREEN)
            break

        while True:
            chapter = get_chapter()
            if chapter.lower() == "q":
                Printer.print_with_style("Please enter manga URL again.", BLUE)
                break

            download_chapter(manga_url, chapter)

if __name__ == "__main__":
    main()
