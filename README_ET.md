# Mõistete Selgitaja

> Koodimiseksperiment LLM-ide buumi algusajast (2023), nüüd täiendatud lokaalse keelemudelite toega.

_Märkus: See dokumentatsioon uuendati 2025. aasta veebruaris kasutades Claude 3.5 Sonnet'i._

See on lihtne tööriist, mis kasutab suuri keelemudeleid (LLM) mõistete selgitamiseks läbi simuleeritud vestluste. Algselt loodi see OpenAI API-ga ChatGPT algse populaarsuse ajal, nüüd on lisatud ka Ollama tugi lokaalseks, võrguühenduseta kasutamiseks.

## Mida see teeb

Võtab sisendiks mõiste, spetsialisti rolli ja sihtgrupi ning genereerib selgituse dialoogi vormis. Näiteks:
- Mõiste: "mustad augud"
- Spetsialist: "astrofüüsik"
- Sihtgrupp: "viieaastane"

Väljund on Markdown formaadis ja sisaldab:
- Põhiselgitus
- Järelküsimused ja vastused
- Võimalusel näited
- Lühike etümoloogia ja ajalugu
- Seotud mõisted

## Võimalused

- Töötab OpenAI API-ga (algne versioon) või Ollamaga (uus 2025)
- Käsurea- ja veebiliides
- Salvestab selgitused Markdown failidena
- Lihtne otsimisfunktsionaalsus

## Paigaldamine

Vajad Python 3.6+ ja kas:
- OpenAI API võtit, või
- Lokaalselt paigaldatud Ollamat (tasuta, töötab võrguühenduseta)

```bash
git clone https://github.com/klauseduard/concept-explainer.git
cd concept-explainer
pip install -r requirements.txt
```

Seadista oma `.env` fail:
```bash
# OpenAI jaoks:
LLM_PROVIDER=openai
OPENAI_API_KEY=sinu-api-võti
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_TEMPERATURE=0.2

# Või Ollama jaoks:
LLM_PROVIDER=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=mistral-small
OLLAMA_TEMPERATURE=0.2
```

## Kasutamine

### Käsuliides

Põhiline käsuformaat:
```bash
python explain.py <mõiste> <spetsialisti_roll> <sihtgrupp> --additional_context <kontekst>
```

Näide:
```bash
python explain.py "mustad augud" "astrofüüsik" "viieaastane" --additional_context "Eelda, et ta teab, mis on tähed."
```

### Veebiliides

Käivita veebiliides:
```bash
python web_interface.py
```

Seejärel ava `http://localhost:5000` oma veebibrauseris.

## Seadistamine

### OpenAI (algne)
- Vajab API võtit
- Vaikimisi mudel: `gpt-3.5-turbo`
- Toetab ka: `gpt-3.5-turbo-0125`, `gpt-4`, `gpt-4-0125`
- Hinnad: https://openai.com/pricing

### Ollama (uus)
- Tasuta, töötab lokaalselt
- Vaikimisi mudel: `mistral-small`
- Töötab ka: `llama2`, `codellama`, `neural-chat`
- API võtit pole vaja
- Vajab arvuti protsessori/graafikakaardi jõudlust

### Temperatuuri seadistus
- Vahemik: 0.0 kuni 2.0 (vaikimisi: 0.2)
- Madalam = fokuseeritum
- Kõrgem = loomingulisem

## Litsents

MIT

## Kontakt

Klaus-Eduard Runnel - klaus.eduard@gmail.com

Projekti link: [https://github.com/klauseduard/concept-explainer](https://github.com/klauseduard/concept-explainer) 