from time import sleep, time
import datetime

from scraper.scraper import get_driver, connect_to_base, parse_html, write_to_file


def run_process(page_number, filename):
    browser = get_driver()
    if connect_to_base(browser, page_number):
        sleep(2)
        html = browser.page_source
        output_list = parse_html(html)
        write_to_file(output_list, filename) 
        browser.quit()
    else:
        print('Error connecting to hackernews')
        browser.quit()


if __name__ == '__main__':
    start_time = time()
    page_number = 1
    output_timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = 'output_{0}.csv'.format(output_timestamp)
    while page_number <= 20:
        run_process(page_number, filename)
        page_number = page_number + 1
    
    end_time = time()
    print('Elapsed run time: {0} seconds'.format(end_time - start_time))