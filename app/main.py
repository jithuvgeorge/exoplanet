import requests
from flask import Flask, render_template
from collections import defaultdict

# configuration
REQUEST_URL = 'https://gist.githubusercontent.com/joelbirchler/66cf8045fcbb6515557347c05d789b4a/raw' \
              '/9a196385b44d4288431eef74896c0512bad3defe/exoplanets'

# create app
app = Flask(__name__)
app.config.from_object(__name__)


def get_orphan_planets_count(content):
    if content is not None:
        return len([p for p in content if p['TypeFlag'] == 3]) or 0
    else:
        return 0


def get_hottest_star_planet(content):
    if content is not None:
        sorted_obj1 = sorted([p for p in content if p['HostStarTempK'] != ""], key=lambda x: int(x['HostStarTempK']),
                             reverse=True)
        if len(sorted_obj1) != 0:
            return sorted_obj1[0].get('PlanetIdentifier', 'default'), sorted_obj1[0].get('HostStarTempK', 'default')
        else:
            return 'default', 'default'
    else:
        return 'default', 'default'


def get_time_line(content):
    if content is not None:
        result = defaultdict(dict)
        for p in content:
            if p['RadiusJpt'] != "" and p['DiscoveryYear'] != "":
                if p['RadiusJpt'] > 2:
                    result[p['DiscoveryYear']]['large'] = result[p['DiscoveryYear']].get('large', 0) + 1
                if 2 > p['RadiusJpt'] > 1:
                    result[p['DiscoveryYear']]['medium'] = result[p['DiscoveryYear']].get('medium', 0) + 1
                if 1 > p['RadiusJpt'] > 0:
                    result[p['DiscoveryYear']]['small'] = result[p['DiscoveryYear']].get('small', 0) + 1
        # print(result.items())
        graph_data = sorted([{'year': str(k), 'Large': result[k].get('large', 0), 'Medium': result[k].get('medium', 0),
                              'Small': result[k].get('small', 0)} for k in dict(result.items())],
                            key=lambda x: int(x['year']))
        return graph_data or 'Empty data'
    else:
        return 'Empty data'


@app.route("/")
def index():
    r = requests.get(app.config["REQUEST_URL"])
    orphan_count = get_orphan_planets_count(r.json())
    hottest_star_planet = get_hottest_star_planet(r.json())
    time_line = get_time_line(r.json())
    data = {'time_line_data': time_line, 'orphan_count': orphan_count, 'hottest_star_planet': hottest_star_planet}
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
