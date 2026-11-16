# 用Python代码快速构建交互式的web网页

import streamlit as st

# 大标题
st.title("Streamlit 入门演示")
st.header('Streamlit 一级标题')
st.subheader('Streamlit 耳机架标题')

# 段落文字
st.write('‌Muse确实能帮你完成支付和购物‌，这是它目前最核心的使用场景之一。它不只是在聊天框里推荐商品，而是能直接替你执行下单、支付这类完整操作。')
st.write('🛒 购物支付怎么运作')
st.write('1.‌全流程代操作‌：你只需说出需求，比如“买一件XX”，Muse会自动打开适配的购物网站或App，完成搜索、比价、加购物车、填地址、提交订单等步骤。')
st.write('2.支付前必确认‌：涉及付款时，Muse会弹出确认请求，每一笔都需要你本人点头，不会擅自扣款。')
st.write('3.支付凭据隔离‌：你的银行卡、支付密码等敏感信息存在独立安全库里，AI本身碰不到，只在网络请求发出瞬间自动替换，降低泄露风险。‌‌')


# 图片

# 音频

# 视频

# 表格

# 输入框
name = st.text_input('请输入姓名')
st.write(f'你输入的姓名为：{name}')
# 单选按钮
