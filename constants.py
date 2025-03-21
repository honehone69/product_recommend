"""
このファイルは、固定の文字列や数値などのデータを変数として一括管理するファイルです。
"""

############################################################
# 共通変数の定義
############################################################

# ==========================================
# 画面表示系
# ==========================================
APP_NAME = "対話型商品レコメンド生成AIアプリ"
USER_ICON_FILE_PATH = "./images/user_icon.jpg"
AI_ICON_FILE_PATH = "./images/ai_icon.jpg"
ERROR_ICON = ":material/error:"
CHAT_INPUT_HELPER_TEXT = "こちらからお探しの商品の特徴や名前を入力してください。"
SPINNER_TEXT = "レコメンドする商品の検討中..."


# ==========================================
# ログ出力系
# ==========================================
LOG_DIR_PATH = "./logs"
LOGGER_NAME = "ApplicationLog"
LOG_FILE = "application.log"
APP_BOOT_MESSAGE = "アプリが起動されました。"

# ==========================================
# Retriever設定系
# ==========================================
TOP_K = 5
RETRIEVER_WEIGHTS = [0.5, 0.5]


# ==========================================
# RAG参照用のデータソース系
# ==========================================
RAG_SOURCE_PATH = "data/products_with_stock.csv"


# ==========================================
# エラー・警告メッセージ
# ==========================================
COMMON_ERROR_MESSAGE = "このエラーが繰り返し発生する場合は、管理者にお問い合わせください。"
INITIALIZE_ERROR_MESSAGE = "初期化処理に失敗しました。"
CONVERSATION_LOG_ERROR_MESSAGE = "過去の会話履歴の表示に失敗しました。"
RECOMMEND_ERROR_MESSAGE = "商品レコメンドに失敗しました。"
LLM_RESPONSE_DISP_ERROR_MESSAGE = "商品情報の表示に失敗しました。"

# 在庫状況の定数
STOCK_LOW = "残りわずか"
STOCK_NONE = "なし"

# 在庫状況メッセージ
STOCK_LOW_MESSAGE = "ご好評につき、在庫数が残りわずかです。購入をご希望の場合、お早めにご注文をおすすめいたします。"
STOCK_NONE_MESSAGE = "申し訳ございませんが、本商品は在庫切れとなっております。入荷までしばらくお待ち下さい。"

# 在庫状況のCSSアイコン
STOCK_LOW_ICON_CSS = """
<div style="display: flex; align-items: center; gap: 8px; color: orange; font-size: 18px;">
    <span style="font-weight: bold;">&#9888;</span> <!-- 三角ビックリマーク -->
    <span>在庫が少なくなっています！</span>
</div>
"""

STOCK_NONE_ICON_CSS = """
<div style="display: flex; align-items: center; gap: 8px; color: red; font-size: 18px;">
    <span style="font-weight: bold;">&#10071;</span> <!-- 丸ビックリマーク -->
    <span>在庫がありません！</span>
</div>
"""
