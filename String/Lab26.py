aboutSimplilearn="""Simplilearn is Trusted by leaders from 100+ Fortune 500 companies and 8 million learners"""
print(aboutSimplilearn)

print(

        "%(edtech)s is Trusted by leaders from %(hundred)s Fortune 500 companies and %(learners)d million learners"
         %{
            'edtech':'API POTHI',
            'hundred':'100+',
            'learners':8,
        }

      )
