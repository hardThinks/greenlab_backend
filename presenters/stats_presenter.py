from typing import Any

from models import Stats


class StatsPresenter:
    def present(self, principal, stats: Stats) -> dict[str, Any]:
        return {
            'total_users': stats.total_users_number,
        }
