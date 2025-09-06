# 👩‍💻 Python People

**Python People** je OOP projekt v Pythonu, který modeluje lidi a jejich role.  
Ukazuje dědičnost, polymorfismus, abstraktní třídu `Clovek` a práci s property a Enum.

---

## 📂 Struktura souborů

- `clovek.py` – abstraktní třída `Clovek` s atributy `jmeno` a `vek`  
- `student.py` – třída `Student` dědící `Clovek`  
- `programator.py` – třída `Programator` dědící `Clovek`  
- `utils.py` – `Enum` s podporovanými programovacími jazyky  
- `run_people.py` – demo skript, ukazuje všechny funkce a polymorfismus  

---

## ✨ Funkce

- 👤 Vytváření lidí s atributy `jmeno`, `vek` a profesí  
- 🔁 Polymorfismus (`pozdrav()`, `chodit()`)  
- 🛡️ Zapouzdření a property (`vek`)  
- 🖥️ Použití Enum pro jazyk programování  
