from ipaddress import ip_address
from general import *
from domain_name import *
from ip_address import *
from nmap import *
from whois import *
from robots_txt import *


ROOT_DIR = 'companies'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + 'full_url.txt', full_url)
    write_file(project_dir + 'full_url.txt', domain_name)
    write_file(project_dir + 'full_url.txt', nmap)
    write_file(project_dir + 'full_url.txt', robots_txt)
    write_file(project_dir + 'full_url.txt', whois)

gather_info('github', 'github.com')