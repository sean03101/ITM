Newsvendor Application Example

+ @김봉석, 이 pdf의 Rmd source 파일도 같은 폴더에 올려주세요.
+ @All, 내용을 굳이 수정해서 보낼 필요는 없고 B_case는 이걸로 마무리 하겠습니다.=. 피드백 참고하세요.

## Feedback

+ 권태현  
    + bullet point 등을 이용해서 문제를 정리하면 좋을 것 같습니다.
    + 문제 설정에 중국과 베트남 중에 하나를 exclusive하게 선택해야 하는지, 그렇다면 그 이유는 무엇인지 내용이 있으면 좋을 것 같습니다.
    + Shipping cost는 어디로 shipping하는 건지, 판매하는 마켓이 우리나라 뿐은 아닐텐데 라는 생각이 듭니다.
    
+ 강의현
    + fish market에 resell을 한다기 보다는 뭐 매운탕이나 튀김을 만드는 형식으로 만드는게 좋을 것 같다는 생각이 드네요.
    
+ 김봉석
    + Newsvendor 모형은 persishable good에 관한 것이므로 (시간이 지나면 가치가 급감), 같은 이유로 항공 분야에도 매우 잘 적용됩니다.
    + 예를들어 400개의 seat가 있는데 티켓을 몇개 파는 것이 좋으냐와 같은 문제에 적용된 예제도 있습니다. (그 이유는 티켓을 구입한 모든 사람이 실제로 비행기 타러 오지는 않으니까요). 이 경우에는 오버부킹이 나서 항공사가 손해를 보는 것과 자리가 비어서 sale을 하지 못하는 두가지 상황을 tradeoff합니다. 
    + 예시로 든 내용도 비슷한 의미에서 적합하지만, 한가지 점은 newsvendor는 계속적으로 반복적으로 일어나는 오퍼레이션을 분석하는 도구로 주로 쓰입니다. 새로운 route의 개척에 newsvendor를 적용하려면 다른 가정이 필요할 것 같습니다.
    
+ 박재민
    + Profit sharing은 supply chain에서 실제로 흔히 등장하는 개념입니다. 숫자를 자세히보지는 않았지만, profit sharing이라는 장치가 suplier와 seller 양쪽의 이익을 동시에 증가시킬수 있다는 결론은 연구에서 내리기에 매우 매력적인 결론입니다.  
    + 이렇게 2개 이상의 economic parties의 이익이 동시에 향상되는 경우를 pareto improvement라고 합니다.
    
+ 손민상
    + 흥미로운 접근입니다. 백신의 수요는 실제로 random이라고 보기 좀 어려울 수도 있지만 (결국 나라로 보아 접종이 필요한 인구는 어느정도 정해져 있으므로) 공급량이 random하다는 가정(아직 초기 생산단계이므로)은 성립할 것 같습니다.
    + 이렇게 정해진 물량을 확보해야 하는 문제를 procurement 문제라고 하는데 매우 적절한 case로 보입니다.
    
+ 권도윤
    + 플라스틱 재활용업자가 플라스틱을 얼마나 구매해야할지의 의사결정에 해당합니다. 그런데 한가지 문제는 플라스틱은 perishable하다고 보기 어렵다는 것입니다. 그렇기 때문에 newsvendor보다는 재고 보관 비용등을 고려한 모델링이 더 좋아보입니다. 마코브체인의(S,s)정책도 여기에 적용될수 있어보입니다.
    
+ 이성호
    + 유행을 잘 타는 의류는 perishable good에 해당합니다. 수영복 보다는 기획상품에 해당하는 뭐... 박보검 티셔츠라던지 그런걸 예시로 들면 문제에 더 적합합니다. 수영복에 비해서 resale value가 낮으니까요.
    
+ 정원렬
    + Describe한 문제는 한정된 자원을 할당하는 문제로 보이고, perishable good이 어떤 것인지 명확하지가 않네요.
    
+ 상지인
    + If PV power isn’t enough to meet the loads’ needs, we should buy electricity from Korea Electric Power
Corporation (KEPCO). On the other hand, if there are unused PV power, we can sell the PV generated
electricity back to KEPCO.
    + 배터리에 전기를 담아두는 것에는 비용이 발생합니다 (베터리에서 전기가 유실되고, 효율이 100%가 아니므로) 
    + 그리고 베터리의 전기가 부족하면 비싼 한전의 전기를 써야되고 배터리의 전기가 남아서 한전에 되팔때 전기를 산 가격에 팔수 없다면 newsvendor 문제 셋팅이 성립합니다.
    + 지적한 대로 PV generation등에 대한 예측이 포함되면 더 좋은 의사결정을 내릴 수 있습니다.
