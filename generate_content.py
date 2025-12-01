from pathlib import Path

base = Path('python_learning_path')

entries = [
    # 0 ZAKLADY
    {
        'path': '00_intro_and_env/00_computer_and_programming_basics',
        'title': 'Počítač a základy programování',
        'bullets': [
            'Co je počítač, hardware vs software',
            'Co je program, zdrojový kód, interpret vs kompilátor',
            'High-level vs low-level jazyk',
            'Jak funguje Python při spuštění skriptu',
        ],
        'examples': [
            "print('Hardware jsou fyzické součásti, software jsou instrukce.')",
            "code = 'print(1 + 1)'; print('Zdrojový kód:', code)",
            "import sys\nprint('Python interpretuje skripty přes', sys.executable)",
        ],
    },
    {
        'path': '00_intro_and_env/01_command_line_and_files',
        'title': 'Příkazová řádka a soubory',
        'bullets': [
            'Terminál, spouštění Python skriptů',
            'Absolutní/relativní cesty',
            'Práce se soubory a složkami',
        ],
        'examples': [
            "import os\nprint('Aktuální adresář:', os.getcwd())",
            "from pathlib import Path\npath = Path('data/example.txt')\nprint('Relativní cesta:', path)\nprint('Absolutní cesta:', path.resolve())",
            "from pathlib import Path\nfolder = Path('ukazka')\nfolder.mkdir(exist_ok=True)\nprint('Vytvořená složka', folder)",
        ],
    },
    {
        'path': '00_intro_and_env/02_python_install_and_venv',
        'title': 'Instalace a virtuální prostředí',
        'bullets': [
            'Instalace Pythonu',
            'Virtuální prostředí (venv)',
            'Aktivace/deaktivace',
            'Instalace balíčků přes pip',
        ],
        'examples': [
            "import sys\nprint('Použitá verze Pythonu:', sys.version)",
            "import venv, pathlib\nvenv_dir = pathlib.Path('moje_venv')\nprint('Adresář pro venv:', venv_dir)",
            "print('pip install requests  # ukázkový příkaz')",
        ],
    },
    # 1 SYNTAXE
    {
        'path': '01_syntax_and_primitives/00_hello_world',
        'title': 'Hello world a struktura skriptu',
        'bullets': [
            'print, komentáře, odsazení',
            'Struktura jednoduchého skriptu',
            'Spouštění přes python název_souboru.py',
        ],
        'examples': [
            "# Jednoduchý výstup\nprint('Ahoj světe!')",
            "# Komentář vysvětluje kód\nprint('Komentáře začínají znakem #')",
            "def main():\n    print('Skript se spouští z funkce main')\n\nif __name__ == '__main__':\n    main()",
        ],
    },
    {
        'path': '01_syntax_and_primitives/01_variables_and_assignment',
        'title': 'Proměnné a přiřazení',
        'bullets': [
            'Proměnné, typy, přiřazování, přepis hodnot',
            'Čitelné názvy proměnných',
            'Kontrola hodnot pomocí print nebo type',
        ],
        'examples': [
            "name = 'Lenka'\nage = 25\nprint('Jméno:', name, 'Věk:', age)",
            "age = age + 1\nprint('Aktualizovaný věk:', age)",
            "value = 3.14\nprint('Typ hodnoty', type(value))",
        ],
    },
    {
        'path': '01_syntax_and_primitives/02_basic_operators',
        'title': 'Základní operátory',
        'bullets': [
            'Aritmetika, //, %, **, porovnání',
            '== vs is',
            'Logické operátory',
        ],
        'examples': [
            "print('Mocnina:', 2 ** 3, 'Modulo:', 10 % 3)",
            "print('Porovnání hodnot:', 3 == 3, 'Identita řetězců:', 'a' is 'a')",
            "is_raining = False\nis_warm = True\nprint('Jdeme ven?', is_warm and not is_raining)",
        ],
    },
    # 2 DATOVE TYPY
    {
        'path': '02_basic_datatypes/00_numeric_types',
        'title': 'Číselné typy',
        'bullets': [
            'int, float, převody, zaokrouhlování',
            'Matematické funkce v modulu math',
            'Bezpečná práce s číselnými vstupy',
        ],
        'examples': [
            "value = 7\nprint('Jako float', float(value))",
            "import math\nprint('Zaokrouhlení', round(3.75), 'Druhá odmocnina', math.sqrt(16))",
            "user_input = '42'\nnumber = int(user_input)\nprint('Převedený vstup', number)",
        ],
    },
    {
        'path': '02_basic_datatypes/01_sequences',
        'title': 'Sekvence a práce s nimi',
        'bullets': [
            'str, list, tuple: indexování, slicing',
            'Změnitelnost vs neměnitelnost',
            'Iterace přes sekvence',
        ],
        'examples': [
            "text = 'Python'\nprint('První písmeno', text[0], 'Řez', text[1:4])",
            "numbers = [1, 2, 3]\nnumbers.append(4)\nprint('List je měnitelný:', numbers)",
            "coords = (10, 20)\nfor value in coords:\n    print('Souřadnice', value)",
        ],
    },
    {
        'path': '02_basic_datatypes/02_mappings_and_sets',
        'title': 'Slovníky a množiny',
        'bullets': [
            'dict, set: klíče, hodnoty, iterace',
            'Typické operace přidání a odebrání',
            'Použití pro rychlé vyhledávání',
        ],
        'examples': [
            "prices = {'jablko': 25, 'banán': 30}\nprint('Cena jablka', prices['jablko'])",
            "seen = set()\nseen.add('uživatel')\nprint('Obsah množiny', seen)",
            "for name, price in prices.items():\n    print(name, '->', price)",
        ],
    },
    {
        'path': '02_basic_datatypes/03_none_and_bool',
        'title': 'None a bool',
        'bullets': [
            'None, pravdivostní hodnota objektů, bool(x)',
            'Rozlišení prázdných hodnot a False',
            'Používání v podmínkách',
        ],
        'examples': [
            "value = None\nprint('Je hodnota nastavena?', value is None)",
            "items = []\nprint('Prázdný list je false?', bool(items))",
            "response = ''\nif not response:\n    print('Nebyl zadán vstup')",
        ],
    },
    {
        'path': '02_basic_datatypes/04_mutable_vs_immutable',
        'title': 'Měnitelné a neměnitelné typy',
        'bullets': [
            'Princip mutability, důsledky v praxi',
            'Kdy kopírovat a kdy sdílet data',
            'Chování při předávání do funkcí',
        ],
        'examples': [
            "original = [1, 2]\ncopy_list = original\ncopy_list.append(3)\nprint('Sdílená reference', original)",
            "name = 'Lenka'\nnew_name = name.replace('L', 'M')\nprint('Řetězec zůstal stejný?', name, '->', new_name)",
            "def add_item(values: list[int]):\n    values.append(99)\n\ndata = [1, 2]\nadd_item(data)\nprint('Výsledek po volání funkce', data)",
        ],
    },
    # 3 FLOW CONTROL
    {
        'path': '03_flow_control/00_if_else_basics',
        'title': 'Podmínky if/elif/else',
        'bullets': [
            'if/elif/else',
            'Pravdivostní výrazy',
            'Idiomatické psaní',
        ],
        'examples': [
            "temperature = 5\nif temperature < 0:\n    print('Mrzne')\nelif temperature < 10:\n    print('Chladno')\nelse:\n    print('Teplo')",
            "value = ''\nif value:\n    print('Něco tu je')\nelse:\n    print('Prázdný řetězec je vyhodnocen jako False')",
            "answer = 'y'\nprint('Souhlas?', 'ano' if answer.lower() == 'y' else 'ne')",
        ],
    },
    {
        'path': '03_flow_control/01_loops_for_while',
        'title': 'Cyklus for a while',
        'bullets': [
            'for přes range a kolekce',
            'while, vhodné použití',
            'Inicializace a podmínky ukončení',
        ],
        'examples': [
            "for number in range(3):\n    print('Opakování', number)",
            "names = ['Eva', 'Adam']\nfor name in names:\n    print('Jméno', name)",
            "counter = 0\nwhile counter < 3:\n    print('While krok', counter)\n    counter += 1",
        ],
    },
    {
        'path': '03_flow_control/02_break_and_continue',
        'title': 'break a continue',
        'bullets': [
            'Předčasné ukončení, přeskočení iterace',
            'Typické scénáře vyhledávání',
            'Čitelné kombinace s podmínkami',
        ],
        'examples': [
            "numbers = [1, 5, 8, 2]\nfor num in numbers:\n    if num > 7:\n        print('Nalezeno číslo > 7:', num)\n        break",
            "for num in numbers:\n    if num % 2 == 0:\n        continue\n    print('Liché číslo', num)",
            "text = 'python'\nfor char in text:\n    if char == 'h':\n        print('Zastavuji u h')\n        break",
        ],
    },
    {
        'path': '03_flow_control/03_enumerate_and_zip',
        'title': 'enumerate a zip',
        'bullets': [
            'Iterace s indexem a přes více kolekcí',
            'Přehlednost oproti ručnímu počítání',
            'Rozbalování hodnot z zip',
        ],
        'examples': [
            "letters = ['a', 'b', 'c']\nfor index, letter in enumerate(letters, start=1):\n    print(index, letter)",
            "names = ['Eva', 'Petr']\nages = [30, 28]\nfor name, age in zip(names, ages):\n    print(name, 'má', age, 'let')",
            "pairs = list(zip(letters, names))\nprint('Spojené páry', pairs)",
        ],
    },
    {
        'path': '03_flow_control/04_all_any_and_predicates',
        'title': 'all, any a predikáty',
        'bullets': [
            'Funkce all, any, predikáty',
            'Vyhodnocení pravdivosti kolekcí',
            'Zkrácené vyhodnocování',
        ],
        'examples': [
            "values = [True, True, False]\nprint('Vše pravda?', all(values))",
            "temperatures = [18, 21, 19]\nprint('Je nějaká teplota nad 20?', any(temp > 20 for temp in temperatures))",
            "users = ['admin', 'guest']\nprint('Všichni mají text?', all(users))",
        ],
    },
    # 4 FUNCTIONS
    {
        'path': '04_functions/00_function_basics',
        'title': 'Základy funkcí',
        'bullets': [
            'def, návratová hodnota, scope, docstring',
            'Vstupní argumenty a pořadí',
            'Pojmenování funkcí podle účelu',
        ],
        'examples': [
            "def greet(name: str) -> str:\n    \"\"\"Vrátí pozdrav pro zadané jméno.\"\"\"\n    return f'Ahoj {name}'\n\nprint(greet('Marie'))",
            "def add(a: int, b: int) -> int:\n    return a + b\n\nprint('Součet', add(2, 3))",
            "message = 'global'\ndef local_example():\n    message = 'lokální'\n    print('Uvnitř', message)\n\nlocal_example()\nprint('Venku', message)",
        ],
    },
    {
        'path': '04_functions/01_default_and_keyword_args',
        'title': 'Výchozí a pojmenované argumenty',
        'bullets': [
            'Výchozí argumenty',
            'Pozor na mutable default',
            'Klíčové argumenty pro čitelnost',
        ],
        'examples': [
            "def greet(name: str, greeting: str = 'Ahoj') -> str:\n    return f'{greeting} {name}'\n\nprint(greet('Eva'))\nprint(greet('Petr', greeting='Zdravím'))",
            "def append_value(value: int, items=None):\n    if items is None:\n        items = []\n    items.append(value)\n    return items\n\nprint(append_value(1))\nprint(append_value(2))",
            "print(greet(name='Lenka', greeting='Čau'))",
        ],
    },
    {
        'path': '04_functions/02_varargs_and_kwargs',
        'title': '*args a **kwargs',
        'bullets': [
            '*args, **kwargs',
            'Sbírání proměnlivého počtu argumentů',
            'Předávání dál do jiných funkcí',
        ],
        'examples': [
            "def sum_numbers(*values: int) -> int:\n    return sum(values)\n\nprint('Součet', sum_numbers(1, 2, 3))",
            "def show_settings(**options):\n    for key, value in options.items():\n        print(key, '->', value)\n\nshow_settings(theme='dark', autosave=True)",
            "def wrap(func, *args, **kwargs):\n    print('Volám funkci...')\n    return func(*args, **kwargs)\n\nprint(wrap(sum_numbers, 4, 5, 6))",
        ],
    },
    {
        'path': '04_functions/03_pure_functions_and_readability',
        'title': 'Čisté funkce a čitelnost',
        'bullets': [
            'Pojmenování, čisté funkce, side-effects',
            'Testovatelnost a předvídatelnost',
            'Kdy logiku rozdělit do menších funkcí',
        ],
        'examples': [
            "def square(number: int) -> int:\n    return number * number\n\nprint(square(5))",
            "history: list[str] = []\ndef add_with_log(a: int, b: int) -> int:\n    result = a + b\n    history.append(result)\n    return result\n\nprint(add_with_log(2, 3), history)",
            "def describe_temperature(value: float) -> str:\n    if value < 0:\n        return 'mráz'\n    if value < 15:\n        return 'chladno'\n    return 'teplo'\n\nprint(describe_temperature(10))",
        ],
    },
    {
        'path': '04_functions/04_modules_and_imports',
        'title': 'Moduly a importy',
        'bullets': [
            'Struktura modulů, import, from ... import ...',
            'Vyhledávací cesta a __name__',
            'Organizace kódu do balíčků',
        ],
        'examples': [
            "import math\nfrom math import sqrt\nprint('Pi:', math.pi, 'Odmocnina 16:', sqrt(16))",
            "print('Aktuální modul:', __name__)",
            "def helper():\n    return 'pomocná funkce v modulu'\n\nif __name__ == '__main__':\n    print(helper())",
        ],
    },
    # 5 NUMBERS
    {
        'path': '05_numbers_and_representation/00_integer_representation_and_overflow',
        'title': 'Reprezentace celých čísel',
        'bullets': [
            'Binární soustava, velikost integeru',
            'Overflow v jiných jazycích vs Python',
            'Konverze do dvojkové soustavy',
        ],
        'examples': [
            "value = 42\nprint('Binárně', bin(value))",
            "big = 10 ** 100\nprint('Velmi velké číslo bez overflow', big)\n",
            "print('Maximální hodnota není pevně omezena, Python dynamicky rozšiřuje.')",
        ],
    },
    {
        'path': '05_numbers_and_representation/01_floats_and_ieee754',
        'title': 'Plovoucí čísla a IEEE 754',
        'bullets': [
            'IEEE 754, běžné chyby s floaty',
            'Přesnost a reprezentace',
            'Ukázka zaokrouhlovacích chyb',
        ],
        'examples': [
            "result = 0.1 + 0.2\nprint('0.1 + 0.2 =', result)",
            "print('Porovnání s 0.3', result == 0.3)",
            "from decimal import Decimal\nprint('Decimal přesnější:', Decimal('0.1') + Decimal('0.2'))",
        ],
    },
    {
        'path': '05_numbers_and_representation/02_rounding_error_and_machine_epsilon',
        'title': 'Zaokrouhlení a strojové epsilon',
        'bullets': [
            'Strojové epsilon, math.isclose',
            'Porovnávání čísel s tolerancí',
            'Praktické dopady při výpočtech',
        ],
        'examples': [
            "import sys, math\nprint('Epsilon pro float:', sys.float_info.epsilon)",
            "a = 0.1 + 0.2\nprint('Je výsledek blízko 0.3?', math.isclose(a, 0.3))",
            "print('Zaokrouhlení', round(2.675, 2))",
        ],
    },
    {
        'path': '05_numbers_and_representation/03_cancellation_and_numerical_stability',
        'title': 'Ztráta přesnosti a stabilita',
        'bullets': [
            'Ztráta přesnosti, přepis vzorců',
            'Vyhýbání se odčítání blízkých čísel',
            'Kontrola výsledků pomocí alternativních výpočtů',
        ],
        'examples': [
            "small = 1e-9\nprint('Odčítání blízkých čísel', (1 + small) - 1)",
            "def stable_mean(values: list[float]) -> float:\n    return sum(values) / len(values)\n\nprint('Průměr', stable_mean([1e6, 1e6 + 1, 1e6 + 2]))",
            "import math\nprint('Použití math.fsum pro lepší přesnost', math.fsum([0.1] * 10))",
        ],
    },
    {
        'path': '05_numbers_and_representation/04_practical_rules_for_floats',
        'title': 'Praktická pravidla pro floaty',
        'bullets': [
            'Jak bezpečně pracovat s floaty',
            'Volba vhodných tolerancí',
            'Formatování a prezentace výsledků',
        ],
        'examples': [
            "value = 1/3\nprint('Formát na tři desetinná místa', f\"{value:.3f}\")",
            "import math\nprint('Porovnání s tolerancí', math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))",
            "result = round(2.3456, 2)\nprint('Zaokrouhleno:', result)",
        ],
    },
    # 6 TYPING
    {
        'path': '06_typing_and_type_system/00_why_and_what_are_type_hints',
        'title': 'Proč a co jsou typové anotace',
        'bullets': [
            'Dynamické typování vs anotace',
            'Přínosy pro čitelnost a nástroje',
            'Základní syntaxe anotací',
        ],
        'examples': [
            "def format_name(name: str) -> str:\n    return name.title()\n\nprint(format_name('petr novak'))",
            "age: int = 30\nprint('Anotovaný věk', age)",
            "def add(a: int, b: int) -> int:\n    return a + b\n\nprint(add(2, 2))",
        ],
    },
    {
        'path': '06_typing_and_type_system/01_basic_annotations',
        'title': 'Základní anotace funkcí',
        'bullets': [
            'Základní anotace funkcí',
            'Anotace návratových hodnot',
            'Komentáře vs skutečné typové kontroly',
        ],
        'examples': [
            "def repeat(text: str, times: int) -> str:\n    return text * times\n\nprint(repeat('ha', 3))",
            "def midpoint(a: float, b: float) -> float:\n    return (a + b) / 2\n\nprint(midpoint(2.0, 4.0))",
            "def shout(message: str) -> None:\n    print(message.upper())\n\nshout('pozdrav')",
        ],
    },
    {
        'path': '06_typing_and_type_system/02_special_types_any_optional_literal_final',
        'title': 'Speciální typy Any, Optional, Literal, Final',
        'bullets': [
            'Any, Optional, Literal, Final',
            'Kdy se hodí širší vs užší typ',
            'Práce s None v anotacích',
        ],
        'examples': [
            "from typing import Any, Optional, Literal, Final\nvalue: Any = 'text'\nmaybe_number: Optional[int] = None\nmode: Literal['r', 'w'] = 'r'\nVERSION: Final = '1.0'\nprint(value, maybe_number, mode, VERSION)",
            "def safe_length(text: Optional[str]) -> int:\n    return len(text) if text is not None else 0\n\nprint(safe_length('abc'))",
            "def use_literal(mode: Literal['light', 'dark']) -> str:\n    return f'Režim: {mode}'\n\nprint(use_literal('light'))",
        ],
    },
    {
        'path': '06_typing_and_type_system/03_generic_collections_and_union',
        'title': 'Generické kolekce a unie',
        'bullets': [
            'Anotace kolekcí (list[int], dict[str, float])',
            'int | float',
            'Čitelné popisy očekávaných hodnot',
        ],
        'examples': [
            "from typing import Union\nprices: dict[str, float] = {'kniha': 249.0}\nvalues: list[Union[int, float]] = [1, 2.5]\nprint(prices, values)",
            "Number = int | float\ndef average(values: list[Number]) -> float:\n    return sum(values) / len(values)\n\nprint(average([1, 2.5, 3]))",
            "from typing import Sequence\ndef first_item(items: Sequence[str]) -> str:\n    return items[0]\n\nprint(first_item(['a', 'b', 'c']))",
        ],
    },
    {
        'path': '06_typing_and_type_system/04_generics_callable_typevar',
        'title': 'Generika, Callable a TypeVar',
        'bullets': [
            'Callable, TypeVar, generika funkcí',
            'Opakovaně použitelná rozhraní',
            'Parametrizace typů pro bezpečnost',
        ],
        'examples': [
            "from typing import Callable, TypeVar\nT = TypeVar('T')\n\ndef apply_twice(func: Callable[[T], T], value: T) -> T:\n    return func(func(value))\n\ndef double(x: int) -> int:\n    return x * 2\n\nprint(apply_twice(double, 3))",
            "from typing import TypeVar\nU = TypeVar('U')\n\ndef identity(value: U) -> U:\n    return value\n\nprint(identity('text'))",
            "from typing import Callable\ndef run_action(action: Callable[[], None]) -> None:\n    action()\n\nrun_action(lambda: print('Volání bez argumentů'))",
        ],
    },
    {
        'path': '06_typing_and_type_system/05_custom_types_alias_newtype_typedict',
        'title': 'Vlastní typy, aliasy a TypedDict',
        'bullets': [
            'Type alias, NewType, TypedDict',
            'Zpřehlednění doménových hodnot',
            'Ochrana proti záměně podobných typů',
        ],
        'examples': [
            "from typing import NewType, TypedDict\nUserId = NewType('UserId', int)\nConfig = TypedDict('Config', {'debug': bool, 'host': str})\nuser_id = UserId(5)\nconfig: Config = {'debug': True, 'host': 'localhost'}\nprint(user_id, config)",
            "AliasScore = int\ndef add_score(score: AliasScore, bonus: AliasScore) -> AliasScore:\n    return score + bonus\n\nprint(add_score(10, 5))",
            "def build_config(debug: bool) -> Config:\n    return {'debug': debug, 'host': '0.0.0.0'}\n\nprint(build_config(False))",
        ],
    },
    # 7 ADVANCED COLLECTIONS
    {
        'path': '07_advanced_collections/00_enums',
        'title': 'Výčtové typy',
        'bullets': [
            'Enum, IntEnum, StrEnum, auto()',
            'Kdy se hodí enumerace',
            'Přiřazení vlastních hodnot',
        ],
        'examples': [
            "from enum import Enum, auto\nclass Mood(Enum):\n    HAPPY = auto()\n    SAD = auto()\n\nprint(Mood.HAPPY)",
            "from enum import IntEnum\nclass Priority(IntEnum):\n    LOW = 1\n    HIGH = 2\n\nprint(Priority.HIGH.value)",
            "for mood in Mood:\n    print('Stav:', mood.name)",
        ],
    },
    {
        'path': '07_advanced_collections/01_counter_and_defaultdict',
        'title': 'Counter a defaultdict',
        'bullets': [
            'Počítání výskytů, implicitní hodnoty',
            'Zjednodušení práce s chybějícími klíči',
            'Praktické příklady agregace',
        ],
        'examples': [
            "from collections import Counter, defaultdict\nwords = ['jablko', 'banán', 'jablko']\ncounts = Counter(words)\nprint(counts)",
            "scores = defaultdict(int)\nscores['Eva'] += 5\nprint('Skóre', dict(scores))",
            "letters = Counter('banana')\nprint('Nejčastější', letters.most_common(1))",
        ],
    },
    {
        'path': '07_advanced_collections/02_chainmap_and_mappingproxy',
        'title': 'ChainMap a MappingProxyType',
        'bullets': [
            'Více vrstev konfigurace',
            'Read-only pohled',
            'Bezpečné sdílení map',
        ],
        'examples': [
            "from collections import ChainMap\ndefaults = {'lang': 'cs'}\noverrides = {'theme': 'dark'}\nconfig = ChainMap(overrides, defaults)\nprint(config['lang'], config['theme'])",
            "from types import MappingProxyType\nsettings = {'mode': 'view'}\nreadonly = MappingProxyType(settings)\nprint(readonly['mode'])",
            "settings['mode'] = 'edit'\nprint('Aktualizovaná hodnota v proxy', readonly['mode'])",
        ],
    },
    {
        'path': '07_advanced_collections/03_namedtuple_and_dataclass',
        'title': 'namedtuple a dataclass',
        'bullets': [
            'Lehká datová schémata',
            'Porovnání s klasickou třídou',
            'Práce s atributy a výchozími hodnotami',
        ],
        'examples': [
            "from collections import namedtuple\nPoint = namedtuple('Point', ['x', 'y'])\np = Point(1, 2)\nprint(p.x, p.y)",
            "from dataclasses import dataclass\n@dataclass\nclass Note:\n    title: str\n    done: bool = False\n\nnote = Note('Nakoupit')\nprint(note)",
            "note.done = True\nprint('Aktualizace dataclass', note)",
        ],
    },
    {
        'path': '07_advanced_collections/04_deque_and_queues',
        'title': 'Fronty s deque',
        'bullets': [
            'deque jako fronta a zásobník',
            'Rychlé přidávání na obou koncích',
            'Praktické scénáře front',
        ],
        'examples': [
            "from collections import deque\nqueue = deque()\nqueue.append('první')\nqueue.append('druhý')\nprint('Odebráno', queue.popleft())",
            "stack = deque()\nstack.append('A')\nstack.append('B')\nprint('Zásobník pop', stack.pop())",
            "queue.extend(['třetí', 'čtvrtý'])\nprint('Obsah fronty', list(queue))",
        ],
    },
    {
        'path': '07_advanced_collections/05_heaps_and_priority_queues',
        'title': 'Halda a prioritní fronta',
        'bullets': [
            'heapq, prioritní fronty',
            'Nejmenší prvek na vrcholu',
            'Použití pro plánování úloh',
        ],
        'examples': [
            "import heapq\nqueue: list[tuple[int, str]] = []\nheapq.heappush(queue, (2, 'úkol B'))\nheapq.heappush(queue, (1, 'úkol A'))\nprint('Pop', heapq.heappop(queue))",
            "heapq.heappush(queue, (3, 'úkol C'))\nheapq.heappush(queue, (0, 'urgentní'))\nprint('Celá fronta', queue)",
            "print('Další v pořadí', queue[0])",
        ],
    },
    {
        'path': '07_advanced_collections/06_arrays_memory_and_bisect',
        'title': 'Pole, paměť a bisect',
        'bullets': [
            'array, memoryview, bisect',
            'Vkládání do seřazených kolekcí',
            'Úspora paměti u velkých dat',
        ],
        'examples': [
            "from array import array\nnumbers = array('i', [1, 2, 3])\nnumbers.append(4)\nprint(numbers.tolist())",
            "data = bytearray(b'abc')\nview = memoryview(data)\nprint('První bajt', view[0])",
            "import bisect\nsorted_values = [1, 3, 5]\nbisect.insort(sorted_values, 4)\nprint(sorted_values)",
        ],
    },
    # 8 OOP
    {
        'path': '08_oop/00_classes_and_instances',
        'title': 'Třídy a instance',
        'bullets': [
            'Třída vs instance',
            'Atributy a konstruktor',
            'Jednoduchá metoda __init__',
        ],
        'examples': [
            "class Person:\n    def __init__(self, name: str):\n        self.name = name\n\n    def greet(self) -> str:\n        return f'Ahoj, jsem {self.name}'\n\nperson = Person('Eva')\nprint(person.greet())",
            "second = Person('Adam')\nprint(second.name)",
            "print('Typ objektu', type(person))",
        ],
    },
    {
        'path': '08_oop/01_instance_vs_class_attributes',
        'title': 'Atributy instance a třídy',
        'bullets': [
            'Atributy třídy vs instance',
            'Sdílené hodnoty mezi instancemi',
            'Kdy použít which pro konstanty',
        ],
        'examples': [
            "class Car:\n    wheels = 4\n\n    def __init__(self, color: str):\n        self.color = color\n\ncar_a = Car('červená')\ncar_b = Car('modrá')\nprint(car_a.wheels, car_b.wheels)",
            "Car.wheels = 3\nprint('Po změně třídy', car_a.wheels, car_b.wheels)",
            "car_a.color = 'zelená'\nprint('Barva A', car_a.color, 'Barva B', car_b.color)",
        ],
    },
    {
        'path': '08_oop/02_magic_methods_basics',
        'title': 'Základní magické metody',
        'bullets': [
            '__str__, __repr__, __len__, __add__, atd.',
            'Vliv na zabudované funkce',
            'Zlepšení ladění a čitelnosti',
        ],
        'examples': [
            "class Bag:\n    def __init__(self, items: list[str]):\n        self.items = items\n\n    def __len__(self) -> int:\n        return len(self.items)\n\n    def __repr__(self) -> str:\n        return f'Bag({self.items!r})'\n\n    def __add__(self, other: 'Bag') -> 'Bag':\n        return Bag(self.items + other.items)\n\nbag = Bag(['pero'])\nprint(len(bag), bag)",
            "second = Bag(['sešit'])\ncombined = bag + second\nprint('Spojená taška', combined)",
            "print('Textová reprezentace', str(combined))",
        ],
    },
    {
        'path': '08_oop/03_public_private_properties',
        'title': 'Veřejné a soukromé atributy',
        'bullets': [
            '_, __, @property, getter/setter',
            'Zapouzdření dat',
            'Kontrola vstupů v settrech',
        ],
        'examples': [
            "class Account:\n    def __init__(self, owner: str):\n        self._owner = owner\n        self.__balance = 0.0\n\n    @property\n    def balance(self) -> float:\n        return self.__balance\n\n    def deposit(self, amount: float) -> None:\n        if amount < 0:\n            raise ValueError('Záporný vklad')\n        self.__balance += amount\n\naccount = Account('Petr')\naccount.deposit(100)\nprint(account.balance)",
            "print('Soukromý atribut je name-mangled', dir(account))",
            "account._owner = 'Eva'\nprint('Změna vlastníka', account._owner)",
        ],
    },
    {
        'path': '08_oop/04_static_and_class_methods',
        'title': 'Statické a třídní metody',
        'bullets': [
            'Statické a třídní metody',
            'Tovární metody z classmethod',
            'Oddělení logiky od stavu instance',
        ],
        'examples': [
            "class Temperature:\n    def __init__(self, celsius: float):\n        self.celsius = celsius\n\n    @staticmethod\n    def c_to_f(celsius: float) -> float:\n        return celsius * 9/5 + 32\n\n    @classmethod\n    def from_fahrenheit(cls, fahrenheit: float) -> 'Temperature':\n        celsius = (fahrenheit - 32) * 5/9\n        return cls(celsius)\n\ntemp = Temperature.from_fahrenheit(68)\nprint(temp.celsius)\nprint(Temperature.c_to_f(20))",
            "print('Použití statické metody bez instance', Temperature.c_to_f(0))",
            "print('Vytvoření z classmethod', Temperature.from_fahrenheit(32).celsius)",
        ],
    },
    {
        'path': '08_oop/05_dataclasses_in_oop',
        'title': 'Dataclass v OOP',
        'bullets': [
            '@dataclass, asdict, srovnání s klasickou třídou',
            'Automaticky generované metody',
            'Jednodušší definice datových objektů',
        ],
        'examples': [
            "from dataclasses import dataclass, asdict\n@dataclass\nclass Book:\n    title: str\n    pages: int\n\nbook = Book('Python', 300)\nprint(book)",
            "print('Jako slovník', asdict(book))",
            "other = Book('Python', 300)\nprint('Porovnání', book == other)",
        ],
    },
    {
        'path': '08_oop/06_iterators_and_generators',
        'title': 'Iterátory a generátory',
        'bullets': [
            'Implementace __iter__, __next__',
            'Generátory pomocí yield',
            'Líné vyhodnocování',
        ],
        'examples': [
            "class Countdown:\n    def __init__(self, start: int):\n        self.current = start\n\n    def __iter__(self):\n        return self\n\n    def __next__(self) -> int:\n        if self.current <= 0:\n            raise StopIteration\n        value = self.current\n        self.current -= 1\n        return value\n\nprint(list(Countdown(3)))",
            "def even_numbers(limit: int):\n    for number in range(0, limit, 2):\n        yield number\n\nprint(list(even_numbers(6)))",
            "generator = (n*n for n in range(3))\nprint(list(generator))",
        ],
    },
    # 9 CODE QUALITY
    {
        'path': '09_code_quality_and_patterns/00_code_smells_overview',
        'title': 'Code smells',
        'bullets': [
            'Co je code smell',
            'Proč to není bug, ale problém designu',
            'Jak je rozpoznat v kódu',
        ],
        'examples': [
            "# Dlouhá funkce jako smell\ndef long_function():\n    parts = []\n    for number in range(5):\n        parts.append(number)\n    return parts\n\nprint(long_function())",
            "# Magické číslo\nPRICE_WITHOUT_MEANING = 42\nprint('Magické číslo', PRICE_WITHOUT_MEANING)",
            "# Duplicitní kód naznačuje refaktoring\nprint('Smelly příklady slouží k diskuzi')",
        ],
    },
    {
        'path': '09_code_quality_and_patterns/01_duplication_long_functions_and_naming',
        'title': 'Duplicitní kód, dlouhé funkce a pojmenování',
        'bullets': [
            'Duplicitní kód, dlouhé funkce, špatné názvy',
            'Rozbití na menší části',
            'Smysluplné názvy proměnných a funkcí',
        ],
        'examples': [
            "def format_price(price_cents: int) -> str:\n    return f'{price_cents / 100:.2f} Kč'\n\nprint(format_price(1999))",
            "def send_welcome_email(user_email: str) -> None:\n    print('Posílám e-mail pro', user_email)\n\nsend_welcome_email('student@example.com')",
            "def summarize(numbers: list[int]) -> int:\n    return sum(numbers)\n\nprint(summarize([1, 2, 3]))",
        ],
    },
    {
        'path': '09_code_quality_and_patterns/02_tight_coupling_and_magic_constants',
        'title': 'Těsné vazby a magické konstanty',
        'bullets': [
            'Tight coupling, dependency injection',
            'Magické konstanty → pojmenované konstanty',
            'Konfigurace pro testovatelnost',
        ],
        'examples': [
            "DEFAULT_TIMEOUT = 5\nAPI_URL = 'https://api.example.com'\nprint('Konstanty jsou na jednom místě')",
            "def fetch_data(url: str, timeout: int = DEFAULT_TIMEOUT) -> None:\n    print(f'Volám {url} s timeoutem {timeout}')\n\nfetch_data(API_URL)",
            "def greet_with_injection(sender: callable) -> None:\n    sender('Ahoj z volané funkce')\n\ngreet_with_injection(print)",
        ],
    },
    {
        'path': '09_code_quality_and_patterns/03_refactoring_techniques',
        'title': 'Refaktoringové techniky',
        'bullets': [
            'Extract method, rename, move method',
            'Postupné malé kroky',
            'Testování po každé změně',
        ],
        'examples': [
            "def calculate_discount(price: float, discount: float) -> float:\n    return price * (1 - discount)\n\nprint(calculate_discount(100, 0.1))",
            "def print_order(items: list[str]) -> None:\n    for item in items:\n        print('-', item)\n\nprint_order(['banán', 'jablko'])",
            "def rename_variable_example():\n    total_price = 10\n    return total_price\n\nprint(rename_variable_example())",
        ],
    },
    {
        'path': '09_code_quality_and_patterns/04_strategy_pattern',
        'title': 'Strategy pattern',
        'bullets': [
            'Eliminace větvení pomocí strategií',
            'Výběr chování za běhu',
            'Jednoduchá kompozice funkcí',
        ],
        'examples': [
            "from typing import Callable\nDiscountStrategy = Callable[[float], float]\n\ndef apply_discount(price: float, strategy: DiscountStrategy) -> float:\n    return strategy(price)\n\ndef no_discount(price: float) -> float:\n    return price\n\ndef student_discount(price: float) -> float:\n    return price * 0.8\n\nprint(apply_discount(100, student_discount))",
            "def seasonal_discount(price: float) -> float:\n    return price * 0.9\n\nprint(apply_discount(200, seasonal_discount))",
            "strategies = {'žák': student_discount, 'bez': no_discount}\nprint(apply_discount(150, strategies['žák']))",
        ],
    },
    {
        'path': '09_code_quality_and_patterns/05_factory_method_pattern',
        'title': 'Factory Method',
        'bullets': [
            'Factory pattern, tvorba objektů',
            'Oddělení konstrukce od použití',
            'Snadná rozšiřitelnost o nové varianty',
        ],
        'examples': [
            "class Message:\n    def __init__(self, text: str):\n        self.text = text\n\n    def send(self) -> None:\n        print('Posílám:', self.text)\n\nclass MessageFactory:\n    @staticmethod\n    def create(text: str) -> Message:\n        return Message(text)\n\nmessage = MessageFactory.create('Ahoj')\nmessage.send()",
            "class Email(Message):\n    def send(self) -> None:\n        print('Email:', self.text)\n\nemail = Email('Vítejte')\nemail.send()",
            "def build_and_send(builder: callable, text: str) -> None:\n    message_obj = builder(text)\n    message_obj.send()\n\nbuild_and_send(MessageFactory.create, 'Factory pattern')",
        ],
    },
]


def intro_text(title: str) -> str:
    return (
        f"Tato lekce představuje téma {title.lower()} a nabízí krátké ukázky, které lze hned spustit. "
        "Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi."
    )


def create_readme(entry: dict, target: Path) -> None:
    intro = intro_text(entry['title'])
    bullets = '\n'.join(f"- {item}" for item in entry['bullets'])
    code_blocks = '\n\n'.join(f"```python\n{code}\n```" for code in entry['examples'][:2])
    tasks = entry.get('tasks')
    if not tasks:
        tasks = [
            f"Vypracujte příklad související s tématem: {entry['bullets'][0]}.",
            f"Napište vlastní variantu, která rozšíří příklady v souboru examples.py.",
            "Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.",
        ]
    tasks_text = '\n'.join(f"- {task}" for task in tasks)
    content = f"""# {entry['title']}

{intro}

## Teorie
{bullets}

## Příklady
{code_blocks}

## Úkoly
{tasks_text}
"""
    target.write_text(content, encoding='utf-8')


def create_examples(entry: dict, target: Path) -> None:
    examples = '\n\n'.join(entry['examples'])
    content = f'''"""Ukázkový kód pro téma {entry['title']}."""

{examples}


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
'''
    target.write_text(content, encoding='utf-8')


def create_exercises(entry: dict, target: Path) -> None:
    tasks = entry.get('tasks')
    if not tasks:
        tasks = [
            f"Vypracujte příklad související s tématem: {entry['bullets'][0]}.",
            f"Doplňte funkci podle rozšířené varianty tématu {entry['title'].lower()}.",
            "Napište verzi, která pracuje s uživatelským vstupem.",
        ]
    functions = []
    base_name = f"lesson_{Path(entry['path']).name}"
    for index, task in enumerate(tasks, start=1):
        name = f"{base_name}_task_{index}"
        doc = (
            f"\"\"\"{task}\n\nVstup i výstup popište dle zadání a doplňte vlastní testovací data.\"\"\""
        )
        functions.append(f"def {name}():\n    {doc}\n    raise NotImplementedError(\"TODO\")\n")
    functions_text = '\n\n'.join(functions)
    header_doc = (
        f"\"\"\"Cvičení k tématu {entry['title']}. Zaměřte se na vlastní implementaci a testování.\"\"\""
    )
    content = f"""{header_doc}

{functions_text}


if __name__ == "__main__":
    # TODO: ručně otestujte funkce
    pass
"""
    target.write_text(content, encoding='utf-8')


def main() -> None:
    for entry in entries:
        folder = base / entry['path']
        folder.mkdir(parents=True, exist_ok=True)
        create_readme(entry, folder / 'README.md')
        create_examples(entry, folder / 'examples.py')
        create_exercises(entry, folder / 'exercises.py')


if __name__ == '__main__':
    main()
