from expecttest import Expect

exps = [
    Expect("""ok"""),
    Expect("""changeme"""),
]

for exp in exps:
    exp.assert_expected("ok")
