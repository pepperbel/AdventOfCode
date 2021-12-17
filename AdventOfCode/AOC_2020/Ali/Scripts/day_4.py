import re
import os
import sys
with open(os.path.join(sys.path[0], "../Inputs/input_day_4.txt"), "r") as my_input:
    _INPUT_1 = my_input.read().replace(" ", "\n")
    _INPUT_1 = _INPUT_1.split("\n\n")


class Passport:
    """I am description"""

    def __init__(self, passport_data):
        self.passport_dict = {
            "byr": self._validate_year_(passport_data.get("byr"), 1920, 2002),
            "iyr": self._validate_year_(passport_data.get("iyr"), 2010, 2020),
            "eyr": self._validate_year_(passport_data.get("eyr"), 2020, 2030),
            "hgt": self._validate_hgt_(passport_data.get("hgt")),
            "hcl": self._validate_hcl_(passport_data.get("hcl")),
            "ecl": self._validate_ecl_(passport_data.get("ecl")),
            "pid": self._validate_pid_(passport_data.get("pid")),
            "cid": self._validate_cid_(passport_data.get("cid"))
        }

    def check_status(self):
        if "INVALID" in self.passport_dict.values():
            return False
        else:
            return True

    def _validate_year_(self, issue_year, min, max):
        if len(issue_year) == 4 and int(issue_year) >= min and int(issue_year) <= max:
            return issue_year
        else:
            return "INVALID"

    def _validate_hgt_(self, height):
        if height[3:] == "cm" and int(height[:3]) >= 150 and int(height[:3]) <= 193:
            return height
        elif height[2:] == "in" and int(height[:2]) >= 59 and int(height[:2]) <= 76:
            return height
        else:
            return "INVALID"

    def _validate_hcl_(self, hair_color):
        hex_chars = "0123456789abcdef"
        if hair_color[0] == "#" and len(hair_color[1:]) == 6:
            for char in hair_color[1:]:
                if char in hex_chars:
                    continue
                else:
                    return "INVALID"
            return hair_color
        else:
            return "INVALID"

    def _validate_ecl_(self, eye_color):
        _VALID_EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if any(eye_color in col for col in _VALID_EYE_COLORS):
            return eye_color
        else:
            return "INVALID"

    def _validate_pid_(self, passport_id):
        passport_id = str(passport_id)
        return (passport_id if len(passport_id) == 9 else "INVALID")

    def _validate_cid_(self, country_id):
        if country_id:
            return country_id
        else:
            return "MISSING"


#----------START------------#
_OUTPUT_1 = 0
_OUTPUT_2 = 0
passports = 0
for passport_data in _INPUT_1:
    passport_data = passport_data.split("\n")
    passport_dict = {}

    if len(passport_data) >= 7:
        for i, entry in enumerate(passport_data):
            entry = entry.split(":")
            passport_dict[entry[0]] = entry[1]
        passports += 1

    if len(passport_dict) == 7 and not passport_dict.get("cid") or len(passport_dict) == 8:
        _OUTPUT_1 += 1
        _PASSPORT = Passport(passport_dict)
        if _PASSPORT.check_status():
            #print("VALID PASSPORT: {}".format(_PASSPORT.passport_dict))
            _OUTPUT_2 += 1


print("Validated Passports 1:", _OUTPUT_1, passports)
print("Validated Passports 2:", _OUTPUT_2, passports)
print(Passport.__doc__)
