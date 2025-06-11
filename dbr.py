from graphviz import Digraph

# Create a directed graph using Graphviz
er = Digraph('ERD', format='png')
er.attr(rankdir='LR', size='8,5')

# 엔터티 정의
entities = {
    "회원": ["회원아이디", "비밀번호", "이름", "나이", "직업", "등급", "적립금"],
    "상품": ["상품번호", "상품명", "재고량", "단가"],
    "제조업체": ["제조업체명", "전화번호", "위치", "담당자"],
    "주문": ["주문번호", "주문수량", "배송지", "주문일자"],
    "게시글": ["글번호", "글제목", "글내용", "작성일자"]
}

# 엔터티와 속성 노드 추가
for entity, attrs in entities.items():
    er.node(entity, shape="box", style="filled", fillcolor="#b3d9ff")
    for attr in attrs:
        attr_node = f"{entity}_{attr}"
        er.node(attr_node, label=attr, shape="ellipse")
        er.edge(attr_node, entity)

# 관계 정의 (마름모 형태)
relations = {
    "주문": [("회원", "n"), ("상품", "m")],
    "공급": [("상품", "n"), ("제조업체", "1")],
    "작성": [("회원", "1"), ("게시글", "n")]
}

# 관계 노드 추가
for rel, participants in relations.items():
    rel_node = f"rel_{rel}"
    er.node(rel_node, label=rel, shape="diamond", style="filled", fillcolor="#e6ccff")
    for ent, cardinality in participants:
        er.edge(ent, rel_node, label=cardinality)
        er.edge(rel_node, ent)

# Save and render
output_path = "/mnt/data/chen_erd_diagram"
er.render(output_path, cleanup=True)
output_path += ".png"