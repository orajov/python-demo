"""Ukázkový kód pro téma ChainMap a MappingProxyType."""

from collections import ChainMap
defaults = {'lang': 'cs'}
overrides = {'theme': 'dark'}
config = ChainMap(overrides, defaults)
print(config['lang'], config['theme'])

from types import MappingProxyType
settings = {'mode': 'view'}
readonly = MappingProxyType(settings)
print(readonly['mode'])

settings['mode'] = 'edit'
print('Aktualizovaná hodnota v proxy', readonly['mode'])


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
