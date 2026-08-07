#!/usr/bin/env python3
"""Wrapper de referencia para skill QuickClaw com entrypoint Python.

COPIE E ADAPTE. Se a sua skill nao executa nada (skill so de prompt), apague
este arquivo — `workspace/` e opcional.

Troque MAIN_SCRIPT pelo seu script e DEPS pelas suas dependencias. O resto
existe por um motivo especifico, explicado abaixo; mexer nele tem custo.

---------------------------------------------------------------------------
As duas regras que este arquivo carrega
---------------------------------------------------------------------------

1. PROPAGAR O EXIT CODE.

   O wrapper e o que o bot executa. Se ele descarta o `returncode` do processo
   filho, sai `0` mesmo com a skill quebrada — e a falha chega ao agente como
   SUCESSO. O agente entao apresenta ausencia de dados como resultado valido.

   Isso nao e hipotese: aconteceu em cinco skills da org em agosto/2026 e
   passou meses sem ninguem ver, porque nao havia nada para ver — nem log,
   nem alerta, nem exit code. `skill-ci` reprova este defeito desde a v1.5.0.

       result = subprocess.run([...])     # capture
       sys.exit(result.returncode)        # e propague

2. DEGRADAR EM SILENCIO E PIOR QUE FALHAR.

   Cair para o Python global quando o `.venv` falha e uma escolha razoavel —
   fazer isso calado nao e. Sem as deps, a skill roda "meio funcionando" e o
   sintoma vira indiagnosticavel. Se voce degrada, AVISE no stderr.
"""

import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
VENV_DIR = SKILL_DIR / ".venv"
VENV_PYTHON = VENV_DIR / "bin" / "python"

# ADAPTE: seu script e suas dependencias.
MAIN_SCRIPT = SKILL_DIR / "workspace" / "main.py"
DEPS = ["requests"]


def _warn(msg):
    """Aviso no stderr. Degradacao silenciosa e indiagnosticavel em campo."""
    print(f"⚠️  {msg}", file=sys.stderr)


FALLBACK = (
    "usando o Python global em vez do .venv da skill — "
    "sem as deps o resultado pode sair incompleto ou vazio."
)


def ensure_venv():
    """Devolve o interpretador a usar, criando o .venv se preciso.

    Revalida os imports mesmo com o .venv presente: um `pip install`
    interrompido (timeout do exec na primeira execucao, por exemplo) deixa o
    venv existente porem inutil, e sem esta checagem a skill roda sem deps.
    """
    if not VENV_PYTHON.exists():
        try:
            subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
        except Exception as e:
            _warn(f"Falha ao criar .venv ({e}); {FALLBACK}")
            return sys.executable

    checagem = subprocess.run(
        [str(VENV_PYTHON), "-c", "import " + ", ".join(DEPS)],
        capture_output=True,
    )
    if checagem.returncode != 0:
        try:
            subprocess.run([str(VENV_PYTHON), "-m", "pip", "install", *DEPS], check=True)
        except Exception as e:
            _warn(f"Falha ao instalar deps no .venv ({e}); {FALLBACK}")
            return sys.executable

    return str(VENV_PYTHON)


def main():
    python_bin = ensure_venv()

    try:
        result = subprocess.run([python_bin, str(MAIN_SCRIPT), *sys.argv[1:]])
    except KeyboardInterrupt:
        print("\n❌ Interrompido.", file=sys.stderr)
        sys.exit(1)

    # NAO REMOVA. Sem esta linha o wrapper sai 0 com a skill quebrada.
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
