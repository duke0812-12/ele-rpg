import streamlit as st
import random

st.set_page_config(page_title="小索的冒險日記", page_icon="🐘")

# 初始化狀態
if 'player_hp' not in st.session_state:
    st.session_state.player_hp = 100
if 'enemy_hp' not in st.session_state:
    st.session_state.enemy_hp = 100
if 'log' not in st.session_state:
    st.session_state.log = []

# 顯示標題與圖片
st.title("🐘 小索的冒險日記：勇闖鬧獸林")
st.image("images/elephant.png", caption="小索準備好了！", use_column_width=True)
st.image("images/goat.png", caption="咩哥看起來不懷好意...", use_column_width=True)

# 顯示血量條
st.progress(st.session_state.player_hp / 100, text=f"小索 HP: {st.session_state.player_hp}")
st.progress(st.session_state.enemy_hp / 100, text=f"咩哥 HP: {st.session_state.enemy_hp}")

# 遊戲按鈕區
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🐘 攻擊"):
        damage = random.randint(15, 25)
        st.session_state.enemy_hp = max(st.session_state.enemy_hp - damage, 0)
        st.session_state.log.append(f"小索揮鼻子造成 {damage} 傷害！")
with col2:
    if st.button("🛡️ 防禦"):
        st.session_state.log.append("小索蹲下防禦！受到的傷害減半。")
        reduced = True
    else:
        reduced = False
with col3:
    if st.button("🍌 吃香蕉"):
        heal = random.randint(10, 20)
        st.session_state.player_hp = min(st.session_state.player_hp + heal, 100)
        st.session_state.log.append(f"小索吃了一根香蕉，回復 {heal} HP！")

# 敵人攻擊回合
if st.session_state.enemy_hp > 0 and st.session_state.player_hp > 0:
    enemy_attack = random.randint(10, 20)
    if reduced:
        enemy_attack = enemy_attack // 2
    st.session_state.player_hp = max(st.session_state.player_hp - enemy_attack, 0)
    st.session_state.log.append(f"咩哥頂了一下小索，造成 {enemy_attack} 傷害！")

# 遊戲結果判斷
if st.session_state.enemy_hp == 0:
    st.success("🎉 小索打敗了咩哥！森林再度和平！")
elif st.session_state.player_hp == 0:
    st.error("💥 小索倒下了...咩哥勝利了！")

# 戰鬥紀錄
st.subheader("📜 戰鬥紀錄")
for entry in st.session_state.log[::-1]:
    st.write(entry)

# 重置按鈕
if st.button("🔁 重新開始"):
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.log = []
    st.experimental_rerun()
