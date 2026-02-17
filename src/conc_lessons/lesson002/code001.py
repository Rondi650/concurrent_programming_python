# Um exemplo de código síncrono que você já conhece bem
from pathlib import Path
import time
import sys

# Adiciona o diretório 'src' ao sys.path
src_path = Path(__file__).parent.parent.parent
print(src_path)
sys.path.insert(0, str(src_path))

from conc_lessons.utils.ansi import Ansi
from conc_lessons.utils.base import (
    get_perftime,
    run_simulated_io,
)

if __name__ == "__main__":
    start_time = time.perf_counter()  # Marca o tempo de início da execução

    run_simulated_io("Work 1", 1, Ansi.pin)  # 1 segundo
    run_simulated_io("Work 2", 1, Ansi.yel)
    run_simulated_io("Work 3", 1, Ansi.gre)

    # É natural que esse código leve aprox. 3 segundos para terminar
    get_perftime(start_time)
