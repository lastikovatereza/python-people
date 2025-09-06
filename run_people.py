from clovek import Clovek
from programator import Programator
from student import Student
from utils import Jazyky

karel = Programator("Karel", 25, "python")

josef = Programator("Josef", 34, "PHP")

karel.pozdrav("Zdravím")
josef.pozdrav()
print(karel.get_jmeno)
karel.set_vek(1000)
karel.set_vek(50)
print(karel.get_vek())

josef.pozdrav("Dobrý večer.")
josef.pozdrav()

lide = [karel, josef]

for clovek in lide:
    clovek.pozdrav()

for clovek in lide:
    print(clovek.jmeno)

for clovek in lide:
    if clovek.vek > 30:
        print(f"{clovek.jmeno} je starší než 30.")

# tyhle metody jsou identické
        # karel == josef
# karel.__eq__(josef)
print(karel)
karel.chodit()

ivan = Student("Ivan", 25 )
ivan.pozdrav()
ivan.chodit()

lucie = Programator("Lucie", 30, Jazyky.PYTHON)
print(lucie.jazyk.value)  # vypíše "Python"
lucie.pozdrav()
