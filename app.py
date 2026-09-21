import streamlit as st
import pandas as pd

st.set_page_config(page_title="幹部選定意思決定支援システム (TeamFit)", layout="wide")

st.title("🎓 サークル幹部選定・多角相性診断システム (TeamFit)")
st.caption("MBTI × 血液型 × DiSC × Big Five × 協働実績 × 人物特徴メモによる意思決定支援")

# ----------------------------------------------------
# サイドバー：設定および評価対象ペアの決定
# ----------------------------------------------------
st.sidebar.header("⚙️ 評価設定")

# 組み合わせ・役職の自由選択
role_options = ["代表", "副代表", "会計", "イベント企画", "広報・SNS", "総務・調整", "技術・コート管理"]

st.sidebar.subheader("📌 診断する役職ペアの選択")
role_a = st.sidebar.selectbox("人物A（リーダー側）の想定役職", role_options, index=0)
role_b = st.sidebar.selectbox("人物B（メンバー側）の想定役職", role_options, index=1)

st.sidebar.markdown("---")

# ----------------------------------------------------
# メイン画面：入力エリア (2カラム構造)
# ----------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"👤 人物A（{role_a} 候補）データ入力")
    name_a = st.text_input("氏名 / ニックネーム", value="A君", key="name_a")
    
    mbti_a = st.selectbox(
        "MBTIタイプ",
        [
            "ENFJ (主人公)", "ENFP (運動家)", "ENTJ (指揮官)", "ENTP (討論者)",
            "INFJ (提唱者)", "INFP (仲介者)", "INTJ (建築家)", "INTP (論理学者)",
            "ESFJ (領事)", "ESFP (エンターテイナー)", "ESTJ (幹部)", "ESTP (起業家)",
            "ISFJ (擁護者)", "ISFP (冒険家)", "ISTJ (管理者)", "ISTP (巨匠)"
        ],
        index=0, key="mbti_a"
    )
    
    blood_a = st.selectbox("血液型", ["A型", "B型", "O型", "AB型"], index=0, key="blood_a")
    
    # DiSC：選択式
    disc_a = st.radio(
        "DiSCタイプ（行動特性）",
        ["D型（Dominance: 主導型・結果重視）", 
         "i型（Influence: 影響型・社交重視）", 
         "S型（Steadiness: 安定型・協調重視）", 
         "C型（Conscientiousness: 慎重型・品質重視）"],
        index=0, key="disc_a"
    )
    
    # Big Five 評価（1〜5段階）
    st.markdown("##### Big Five 評価 (1〜5段階)")
    ext_a = st.slider("外向性（明るさ・社交性）", 1, 5, 4, key="ext_a")
    agr_a = st.slider("協調性（優しさ・配慮）", 1, 5, 5, key="agr_a")
    con_a = st.slider("勤勉性/誠実性（計画性・几帳面さ）", 1, 5, 3, key="con_a")
    neu_a = st.slider("神経質傾向（メンタルの繊細さ・不安の感じやすさ）", 1, 5, 2, key="neu_a")
    ope_a = st.slider("開放性（好奇心・柔軟性）", 1, 5, 4, key="ope_a")
    
    st.markdown("##### 過去の関わり度（直感評価）")
    rel_a = st.select_slider(
        "お互いをどの程度知っているか・協働経験",
        options=[
            "1:【ほぼ接点なし】話したことが少ない",
            "2:【あまり知らない】顔と名前を知る程度",
            "3:【ふつう】サークル内で雑談する程度",
            "4:【けっこう知っている】イベント等で協力経験あり",
            "5:【超バッチリ】仕事の癖や考え方まで把握"
        ],
        value="4:【けっこう知っている】イベント等で協力経験あり",
        key="rel_a"
    )

    st.markdown("##### 📝 人物の特徴・特記事項（メモ）")
    notes_a = st.text_area(
        "個人の性質・強み・注意点など（例：リーダーシップがある、人前に出るのが得意、酒癖に注意 等）",
        value="リーダーシップがあり周りを引っ張るのが得意。理想が高いが少し大雑把な一面あり。",
        key="notes_a"
    )


with col2:
    st.subheader(f"👤 人物B（{role_b} 候補）データ入力")
    name_b = st.text_input("氏名 / ニックネーム", value="B君", key="name_b")
    
    mbti_b = st.selectbox(
        "MBTIタイプ",
        [
            "ENFJ (主人公)", "ENFP (運動家)", "ENTJ (指揮官)", "ENTP (討論者)",
            "INFJ (提唱者)", "INFP (仲介者)", "INTJ (建築家)", "INTP (論理学者)",
            "ESFJ (領事)", "ESFP (エンターテイナー)", "ESTJ (幹部)", "ESTP (起業家)",
            "ISFJ (擁護者)", "ISFP (冒険家)", "ISTJ (管理者)", "ISTP (巨匠)"
        ],
        index=5, key="mbti_b" # デフォルト INFP
    )
    
    blood_b = st.selectbox("血液型", ["A型", "B型", "O型", "AB型"], index=2, key="blood_b")
    
    # DiSC：選択式
    disc_b = st.radio(
        "DiSCタイプ（行動特性）",
        ["D型（Dominance: 主導型・結果重視）", 
         "i型（Influence: 影響型・社交重視）", 
         "S型（Steadiness: 安定型・協調重視）", 
         "C型（Conscientiousness: 慎重型・品質重視）"],
        index=2, key="disc_b" # デフォルト S型
    )
    
    # Big Five 評価（1〜5段階）
    st.markdown("##### Big Five 評価 (1〜5段階)")
    ext_b = st.slider("外向性（明るさ・社交性）", 1, 5, 2, key="ext_b")
    agr_b = st.slider("協調性（優しさ・配慮）", 1, 5, 5, key="agr_b")
    con_b = st.slider("勤勉性/誠実性（計画性・几帳面さ）", 1, 5, 4, key="con_b")
    neu_b = st.slider("神経質傾向（メンタルの繊細さ・不安の感じやすさ）", 1, 5, 4, key="neu_b")
    ope_b = st.slider("開放性（好奇心・柔軟性）", 1, 5, 3, key="ope_b")
    
    st.markdown("##### 過去の関わり度（直感評価）")
    rel_b = st.select_slider(
        "お互いをどの程度知っているか・協働経験",
        options=[
            "1:【ほぼ接点なし】話したことが少ない",
            "2:【あまり知らない】顔と名前を知る程度",
            "3:【ふつう】サークル内で雑談する程度",
            "4:【けっこう知っている】イベント等で協力経験あり",
            "5:【超バッチリ】仕事の癖や考え方まで把握"
        ],
        value="3:【ふつう】サークル内で雑談する程度",
        key="rel_b"
    )

    st.markdown("##### 📝 人物の特徴・特記事項（メモ）")
    notes_b = st.text_area(
        "個人の性質・強み・注意点など（例：簿記所持、人前に出るのが苦手、酒癖が悪い 等）",
        value="共感力が高くメンバーの相談によく乗る。人前に立つのや厳しい注意は苦手。日商簿記2級所持。",
        key="notes_b"
    )

st.markdown("---")

# ----------------------------------------------------
# 診断ロジック・解析ボタン
# ----------------------------------------------------
if st.button("🚀 多角相性・役職適合度解析を実行する", type="primary", use_container_width=True):
    
    # 簡易スコアリング計算ロジック
    mbti_code_a = mbti_a[:4]
    mbti_code_b = mbti_b[:4]
    
    score_mbti = 70
    # MBTI 補完チェック
    if mbti_code_a[0] != mbti_code_b[0]: score_mbti += 10 # E/I 補完
    if mbti_code_a[1] == mbti_code_b[1]: score_mbti += 10 # N/S 共通言語
    if mbti_code_a[2] != mbti_code_b[2]: score_mbti += 10 # T/F 補完
    
    # F型同士の注意ペナルティ（論文の理論より）
    if mbti_code_a[2] == 'F' and mbti_code_b[2] == 'F':
        score_mbti -= 15
        
    score_mbti = min(100, max(30, score_mbti))
    
    # Big Five 勤勉性補正（計画性が高いペアは組織運営で有利）
    bigfive_bonus = (con_a + con_b) * 2
    
    # 関わり度スコア（数字のみ抽出）
    rel_score_num = int(rel_a[0])
    rel_score_total = rel_score_num * 20 # 100点満点換算
    
    # 総合スコア（MBTI 50%, 関わり度 35%, Big Five補正 15%）
    total_score = int(score_mbti * 0.5 + rel_score_total * 0.35 + bigfive_bonus * 1.5)
    total_score = min(100, max(10, total_score))
    
    # 結果表示
    st.header("📊 総合解析結果")
    
    st.metric(
        label=f"【{role_a}】{name_a} × 【{role_b}】{name_b} のチーム適合度",
        value=f"{total_score} %",
        delta="最適配置" if total_score >= 75 else ("要ワンクッション" if total_score >= 50 else "リスク高")
    )
    
    st.markdown("---")
    
    col_res1, col_res2 = st.columns(2)
    
    with col_res1:
        st.subheader("💡 診断データ要約")
        st.write(f"・**ペア組み合わせ:** {role_a}（{name_a}） × {role_b}（{name_b}）")
        st.write(f"・**MBTI基本相性:** {score_mbti} 点")
        st.write(f"・**DiSC組み合わせ:** {disc_a[:2]} × {disc_b[:2]}")
        st.write(f"・**Big Five 勤勉性合計:** {con_a + con_b} / 10")
        st.write(f"・**血液型ペア:** {blood_a} × {blood_b}")
        st.write(f"・**相互認知・関わり度:** レベル {rel_score_num} / 5")

        st.markdown("##### 📌 入力された特記事項・人物特徴")
        st.info(f"**【{name_a}（{role_a}）のメモ】**\n{notes_a}")
        st.info(f"**【{name_b}（{role_b}）のメモ】**\n{notes_b}")

    with col_res2:
        st.subheader("📖 組織行動学・RAG経験知アドバイス")
        
        if total_score >= 75:
            st.success("🟢 **【非常に良好なパートナーシップ】**\n\n価値観や役割補完が機能しており、組織の安定が見込めます。特に特徴メモにある強みを活かした役割分担（例：会計作業や企画の割り振り）を行うことでパフォーマンスが最大化されます。")
        elif total_score >= 50:
            st.warning("🟡 **【要クッション（サポート役が必要）】**\n\n共感力が高く雰囲気は良好ですが、優しすぎるあまり「厳しい指摘や規律の維持」がおろそかになる構造的盲点があります。特徴メモにある「人前に出るのが苦手」「酒癖注意」などのリスクに対応するため、ロジカルに仕切れる『第3の人物（補佐・会計等）』を幹部会に加えることを推奨します。")
        else:
            st.error("🔴 **【慎重な役割配置を推奨】**\n\n行動テンポや思考プロセスの乖離が大きく、双方にストレスがかかる可能性があります。別の役職への配置転換か、間を取り持つ強力な仲介者を設置してください。")

        # 特記事項に基づいたリアルタイムチェックメッセージ
        if "酒" in notes_a or "酒" in notes_b:
            st.warning("⚠️ **特記事項アラート:** コンプライアンスや飲み会運営ルールを事前に定めておくことを推奨します。")
        if "簿記" in notes_b or "会計" in notes_b:
            st.info("💡 **特記事項ピックアップ:** B君の「簿記」スキルは会計係や予算管理として大きな強みになります。")
