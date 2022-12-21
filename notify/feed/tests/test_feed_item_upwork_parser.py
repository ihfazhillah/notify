from notify.feed.util import parse_upwork_feed

example = """
Hi,<br /> I need a Server Guy. Someone that can help me to quickly install and configure the web apps that I develop. Someone that can quickly fix prolems and suggests the best options related to security and performance.<br /> Apps are written in django so some previous experience in this kind of project would be a plus. <br /><br /><b>Hourly Range</b>: $10.00-$25.00 <br /><b>Posted On</b>: December 18, 2022 12:55 UTC<br /><b>Category</b>: Systems Administration<br /><b>Skills</b>:Python, Linux, Ubuntu, System Administration, Linux System Administration, Apache HTTP Server, NGINX, Django <br /><b>Country</b>: Brazil <br /><a href="https://www.upwork.com/jobs/Server-Administrator-Linux-django-web-apps_%7E01351ade72647ef3e9?source=rss">click to apply</a>
"""


def test_parse_example():
    result = parse_upwork_feed(example)
    keys = [
        "description", "posted_on", "category", "skills", "hourly_range", "country"
    ]
    assert sorted(list(result.keys())) == sorted(keys)


