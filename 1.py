import json

def namaUmur(name, age):
    biodata = {
        "name" : name,
        "age" : age,
        "address" : "Rejo Agung, Kecamatan Tegineneng, Kabupaten Pesawaran, Lampung",
        "hobbies" : ["Reading","Writing"],
        "is_married" : False,
        "list_school" : [
            {
                "name" : "SD Negeri 1 Rejo Agung",
                "year_in" : 2002,
                "year_out" : 2008,
                "major" : "null"
            },
            {
                "name" : "MTs Nurul Iman",
                "year_in" : 2008,
                "year_out" : 2011,
                "major" : "null"
            },
            {
                "name" : "MA Negeri 2 Metro",
                "year_in" : 2011,
                "year_out" : 2014,
                "major" : "Ilmu Pengetahuan Alam"
            },
            {
                "name" : "Universitas Lampung",
                "year_in" : 2014,
                "year_out" : 2019,
                "major" : "Teknik Elektro"
            }
        ],
        "skills" : [
            {
                "skill_name" : "Microsoft Word",
                "level" : "advanced"
            },
            {
                "skill_name" : "Microsoft excel",
                "level" : "advanced"
            },
            {
                "skill_name" : "Microsoft PPT",
                "level" : "advanced"
            },
            {
                "skill_name" : "Microsoft Visio",
                "level" : "advanced"
            },
            {
                "skill_name" : "MATLAB",
                "level" : "beginner"
            }
            ],
        "interest_in_coding" : True
    }

    x = json.dumps(biodata)

    print(x)

namaUmur("Sahrul Kais", 23)