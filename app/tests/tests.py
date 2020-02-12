import unittest
from app import main
from app.main import app


class BasicTestCase(unittest.TestCase):
    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code, 200)


class MainTestCase(unittest.TestCase):
    empty_dict = {}
    none_dict = None
    planet_dict = [
        {
            "PlanetIdentifier": "CFBDSIR2149",
            "TypeFlag": 3,
            "RadiusJpt": "",
            "DiscoveryYear": 2016,
            "HostStarTempK": ""
        },
        {
            "PlanetIdentifier": "CFBDSIR2150",
            "TypeFlag": 2,
            "RadiusJpt": .09,
            "DiscoveryYear": 2012,
            "HostStarTempK": "222"
        }]

    def test_empty_orphan_count(self):
        assert main.get_orphan_planets_count(self.empty_dict) == 0

    def test_empty_hottest_star_planet(self):
        assert main.get_hottest_star_planet(self.empty_dict)[0] == 'default'

    def test_empty_time_Line(self):
        assert main.get_time_line(self.empty_dict) == 'Empty data'

    def test_none_orphan_count(self):
        assert main.get_orphan_planets_count(self.none_dict) == 0

    def test_none_hottest_star_planet(self):
        assert main.get_hottest_star_planet(self.none_dict)[0] == 'default'

    def test_none_time_Line(self):
        assert main.get_time_line(self.none_dict) == 'Empty data'

    def test_orphan_count(self):
        assert main.get_orphan_planets_count(self.planet_dict) == 1

    def test_hottest_star_planet(self):
        assert main.get_hottest_star_planet(self.planet_dict)[0] == 'CFBDSIR2150'

    def test_time_Line(self):
        assert len(main.get_time_line(self.planet_dict)) == 1


if __name__ == '__main__':
    unittest.main()
