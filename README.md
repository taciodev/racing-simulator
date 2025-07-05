# 🏁 Simulador de Corrida com Threads

Este é um projeto simples em Python que simula uma corrida entre carros usando threads, zonas críticas (com mutex) e atualizações visuais no terminal com emojis.

---

## 📦 Requisitos

- Python 3.10 ou superior
- [uv](https://github.com/astral-sh/uv) instalado

> O `uv` é um gerenciador de pacotes Python moderno e super rápido. Para instalar:

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

## ▶️ Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/race_simulation.git
cd race-simulation
```

2. Crie o ambiente virtual com `uv`:

```bash
uv venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate    # Windows
```

3. Execute o programa:

```bash
python main.py
```

---

## 📁 Estrutura do Projeto

```
race-simulation/
├── main.py
├── models/
│   ├── circuit.py
│   ├── car.py
│   └── race.py
```

---

## 🛠️ Funcionalidades

- Corrida com múltiplos carros em threads
- Exibição em tempo real com emojis no terminal
- Largada sincronizada
- Zona crítica com exclusão mútua (mutex)
- Clima afeta a velocidade dos carros

---

## 📄 Licença

MIT
