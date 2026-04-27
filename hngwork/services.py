import requests

class ExternalAPIService:
    @staticmethod
    def get_gender(name):
        url = f"https://api.genderize.io?name={name}"
        res = requests.get(url) . json()

        if not res.get("gender") or res.get("county") == 0:
           raise Exception("Genderize returned an invalid response")


        return{
                "gender": res["gender"],
                "gender_probability": res["probability"],
                "sample_size": res["count"],

            }
    
    @staticmethod
    def get_age(name):
        url = f"https://api.agify.io?name={name}"
        res = requests.get(url).json()

        if res.get("age") is None:
            raise Exception("Agify returned an invalid response")

        age = res["age"]

        if age <= 12:
            age_group = "child"
        elif age <= 19:
            age_group = "teenager"
        elif age <= 59:
            age_group = "adult"
        else:
            age_group = "senior"

        return {
            "age": age,
            "age_group": age_group
        }


    @staticmethod
    def get_country(name):
        url = f"https://api.nationalize.io?name={name}"
        res = requests.get(url).json()

        countries = res.get("country", [])
        if not countries:
                raise Exception("Nationalize returned an invalid response")

        best = max(countries, key=lambda x: x["probability"])

        return {
                "country_id": best["country_id"],
                "country_probability": best["probability"]
            }
