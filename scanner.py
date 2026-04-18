#!/usr/bin/env python3
"""
Polymarket Scanner v2 — кросс-проверка с реальными спортивными результатами.
Два уровня: СНАЙПЕР (результат известен) и СИГНАЛ (высокая уверенность).
Запускается каждые 20 минут через cron.
"""

import urllib.request
import urllib.parse
import json
import ssl
import os
from datetime import datetime, timezone

# ─── CONFIG ───────────────────────────────────────────────────────────────────
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID", "")

SNIPER_CONFIDENCE  = 0.90   # порог для СНАЙПЕР
SIGNAL_CONFIDENCE  = 0.88   # порог для СИГНАЛ
MAX_HOURS          = 168    # 7 дней
MIN_VOLUME         = 5000

SEEN_FILE = "/root/polymarket_scanner/seen.json"

# Слова-фильтры — такие рынки пропускаем (мусор/спам)
SKIP_KEYWORDS = [
    'nfl draft', 'first pick', 'art ross', 'rocket richard',
    'calder', 'vezina', 'norris trophy', 'hart memorial',
    'before gta vi', 'hit $1m', 'hit $150k',
]

# Команды NHL для матчинга с ESPN
NHL_TEAMS = {
    'oilers': 'EDM', 'canucks': 'VAN', 'flames': 'CGY', 'jets': 'WPG',
    'avalanche': 'COL', 'golden knights': 'VGK', 'kings': 'LAK',
    'ducks': 'ANA', 'sharks': 'SJS', 'kraken': 'SEA',
    'stars': 'DAL', 'blues': 'STL', 'predators': 'NSH', 'mammoth': 'UTA',
    'lightning': 'TBL', 'panthers': 'FLA', 'hurricanes': 'CAR',
    'bruins': 'BOS', 'sabres': 'BUF', 'canadiens': 'MTL', 'senators': 'OTT',
    'maple leafs': 'TOR', 'rangers': 'NYR', 'islanders': 'NYI', 'devils': 'NJD',
    'flyers': 'PHI', 'penguins': 'PIT', 'capitals': 'WSH', 'blue jackets': 'CBJ',
    'red wings': 'DET', 'blackhawks': 'CHI', 'wild': 'MIN', 'coyotes': 'ARI',
}

NBA_TEAMS = {
    'lakers': 'LAL', 'warriors': 'GSW', 'celtics': 'BOS', 'nuggets': 'DEN',
    'thunder': 'OKC', 'suns': 'PHX', 'clippers': 'LAC', 'mavericks': 'DAL',
    'grizzlies': 'MEM', 'pelicans': 'NOP', 'spurs': 'SAS', 'rockets': 'HOU',
    'jazz': 'UTA', 'trail blazers': 'POR', 'blazers': 'POR',
    'heat': 'MIA', 'bucks': 'MIL', 'hawks': 'ATL', 'hornets': 'CHA',
    'wizards': 'WAS', 'nets': 'BKN', 'knicks': 'NYK', '76ers': 'PHI',
    'raptors': 'TOR', 'cavaliers': 'CLE', 'pacers': 'IND', 'pistons': 'DET',
    'bulls': 'CHI', 'magic': 'ORL',
}

MLB_TEAMS = {
    'yankees': 'NYY', 'red sox': 'BOS', 'blue jays': 'TOR', 'orioles': 'BAL',
    'rays': 'TB', 'white sox': 'CWS', 'guardians': 'CLE', 'tigers': 'DET',
    'royals': 'KC', 'twins': 'MIN', 'astros': 'HOU', 'rangers': 'TEX',
    'athletics': 'OAK', 'mariners': 'SEA', 'angels': 'LAA',
    'dodgers': 'LAD', 'giants': 'SF', 'padres': 'SD', 'diamondbacks': 'ARI',
    'rockies': 'COL', 'braves': 'ATL', 'mets': 'NYM', 'phillies': 'PHI',
    'marlins': 'MIA', 'nationals': 'WSH', 'cubs': 'CHC', 'cardinals': 'STL',
    'brewers': 'MIL', 'reds': 'CIN', 'pirates': 'PIT',
}
# ──────────────────────────────────────────────────────────────────────────────

def get_opener():
    ...

def load_seen():
    ...

def save_seen(seen):
    ...

# ── ESPN APIs ─────────────────────────────────────────────────────────────────

def get_espn_scores(sport):
    """Возвращает завершённые игры {(team1, team2): winner}"""
    ...

def find_winner_for_question(question, sport_results, team_dict):
    """Пробует найти победителя для вопроса рынка."""
    ...

# ── Polymarket ────────────────────────────────────────────────────────────────

def is_garbage(question):
    ...

def scan_polymarket():
    ...

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    ...

def send_telegram(text):
    ...

if __name__ == '__main__':
    main()
