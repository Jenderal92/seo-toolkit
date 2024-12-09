import argparse
from crawler import crawl_website
from analyzer import analyze_keyword_density
from report_generator import generate_report

BANNER = """
========================================
           SIMPLE SEO TOOLKIT 1.0
  Advanced Tools for Web Optimization
========================================
"""

def main():
    print BANNER
    parser = argparse.ArgumentParser(description="SEO Toolkit - Command Line Tool")
    parser.add_argument("url", help="URL of the website to analyze")
    parser.add_argument("-o", "--output", help="File to save the SEO report", default="report.txt")
    args = parser.parse_args()

    print "[INFO] Crawling website..."
    links = crawl_website(args.url)
    print "[INFO] Found {} links.".format(len(links))

    print "[INFO] Analyzing keyword density..."
    keyword_density = analyze_keyword_density(" ".join(links))

    print "[INFO] Generating report..."
    generate_report(keyword_density, args.output)

if __name__ == "__main__":
    main()
