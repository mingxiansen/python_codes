# -*- coding:utf-8 -*-
import json
data = {'"2016-11-26":"<li>招聘会：<a target="_blank" href="\/jobfair\/view\/id\/26660">江苏省百校联动-江南大学2017届毕业生供需见面会<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120094">美特科技（苏州）有限公司<\/a><\/li>","2016-11-11":"<li>招聘会：<a target="_blank" href="\/jobfair\/view\/id\/26783">江南大学纺织服装学院2017届毕业生 企业专场招聘会邀请函<\/a><\/li><li>招聘会：<a target="_blank" href="\/jobfair\/view\/id\/26831">江南大学设计学院2017届毕业生设计类专场招聘会<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118768">绿雪生物工程（深圳）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/116228">上海广亩景观设计有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121824">上海金地物业服务有限公司南京分公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121551">浙江龙盛集团股份有限公司技术中心<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121889">研华科技（中国）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122348">无锡悦馨生物科技有限公司<\/a><\/li>","2016-11-18":"<li>招聘会：<a target="_blank" href="\/jobfair\/view\/id\/27047">江南大学商学院2017届毕业生专场招聘会<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/119346">菱王电梯股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122077">浙江博多投资管理有限公司<\/a><\/li>","2016-11-25":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122393">基斯顿食品集团<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117477">奥飞娱乐股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120675">仙乐健康科技股份有限公司<\/a><\/li>","2016-11-1":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122408">江苏恒顺集团有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/116112">宏胜饮料集团<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/113798">前锦网络信息技术（上海）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/114283">格林美股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117459">京东方科技集团股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118693">江苏省通信服务有限公司网盈分公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121075">吴江近岸蛋白质科技有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121543">上海美吉生物医药科技有限公司<\/a><\/li>","2016-11-7":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120057">江苏国泰国际集团国贸股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/116561">赫比（上海）家用电器产品有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121753">浙江舒工坊针纺有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/115999">杭州味全食品有限公司<\/a><\/li>","2016-11-15":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/112623">上海徐汇区韦博进修学校<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121111">海澜集团有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117881">义乌华鼎锦纶股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118864">浙江青莲食品股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122332">天王电子（深圳）有限公司<\/a><\/li>","2016-11-4":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/113565">江苏英科医疗制品有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118501">九牧厨卫股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120083">达能（中国）食品饮料有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122091">苏州鼎酷通讯电子有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121211">无锡欧典空间装饰工程有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122055">陆家嘴国泰人寿保险有限责任公司江苏分公司无锡营销服务部<\/a><\/li>","2016-11-23":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122066">苏州链家房地产经纪有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/116876">江苏曲速教育科技有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117823">快尚时装（广州）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121094">苏州美盈森环保科技有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121548">领胜城科技（江苏）有限公司<\/a><\/li>","2016-11-8":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/112956">杭州新东方进修学校<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/114409">佛吉亚（无锡）座椅部件有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118570">无锡万斯家居用品有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118827">苏州崇邦新基企业管理咨询有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120184">江苏苏豪国际集团股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122169">华孚色纺股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122056">上海玺飞航空技术有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122700">唯品会（昆山）电子商务有限公司<\/a><\/li>","2016-11-10":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/119054">南通联亚药业有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117005">飒拉商业（上海）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/119927">南京链家房地产经纪有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118907">安正时尚集团股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120356">华奥泰<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120925">鲁泰纺织股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122102">建发（上海）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122212">蓝鸽集团有限公司<\/a><\/li>","2016-11-3":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/113535">融创物业服务集团有限公司无锡分公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120777">中兴智能交通股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/115912">联化科技股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118106">无锡新东方进修学校<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118697">安德普翰人力资源服务（上海）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118581">中化（青岛）实业有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118904">锦江麦德龙现购自运有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121148">上海安绚信息技术有限公司<\/a><\/li>","2016-11-2":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/113445">佛山市海天调味食品股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/113690">江苏亚威机床股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/116065">瑞银企业管理（上海）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117502">上海博越服饰有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122468">上海永升物业管理有限公司苏州分公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118155">上海桃李食品有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120766">绿点（苏州）科技有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120170">四川古蔺郎酒销售有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121755">北京外企人力资源服务江苏有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122428">江苏南瑞恒驰电气装备有限公司<\/a><\/li>","2016-11-5":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/113501">中荣印刷（昆山）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120525">海信（浙江）空调有限公司<\/a><\/li>","2016-11-17":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/114264">江苏百胜电子有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120433">北京东升博展科技发展有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120029">安徽古井集团有限责任公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122526">江苏无锡欧派集成家居有限公司<\/a><\/li>","2016-11-9":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/114446">江苏苏美达轻纺国际贸易有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/115172">宝时得科技（中国）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118339">好想你枣业股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118625">远东控股集团有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118710">南京康尼机电股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121969">汉腾汽车有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122002">德国科德宝集团  2016秋季校园<\/a><\/li>","2016-11-22":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/114947">震旦（中国）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121218">鲁南制药集团股份有限公司<\/a><\/li>","2016-11-14":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/119398">上海三枪（集团）有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/118537">南京烽火星空通信发展有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122524">江苏纳思书院教育科技有限公司无锡分公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122096">江苏千米网络科技股份有限公司<\/a><\/li>","2016-11-6":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117438">热风投资有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121246">国金黄金股份有限公司<\/a><\/li>","2016-11-21":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/117744">亨通集团有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121241">宝供物流企业集团有限公司<\/a><\/li>","2016-11-12":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122083">浙江传化股份有限公司<\/a><\/li>","2016-11-24":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121881">奥瑞金包装股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121679">上海清轩生物科技有限公司<\/a><\/li>","2016-11-16":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122221">广东奇化化工交易中心股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/120617">无锡贝斯特精机股份有限公司<\/a><\/li><li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121000">浙江新和成股份有限公司<\/a><\/li>","2016-11-27":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/121916">四川航空股份有限公司<\/a><\/li>","2016-11-28":"<li>宣讲会：<a target="_blank" href="\/teachin\/view\/id\/122582">苏州旭悦置业有限公司<\/a><\/li>","hasTeachin":{"2016-11-25":3,"2016-11-1":8,"2016-11-7":4,"2016-11-15":5,"2016-11-4":6,"2016-11-23":5,"2016-11-8":8,"2016-11-10":8,"2016-11-3":8,"2016-11-2":10,"2016-11-5":2,"2016-11-17":4,"2016-11-9":7,"2016-11-11":6,"2016-11-22":2,"2016-11-14":4,"2016-11-6":2,"2016-11-21":2,"2016-11-12":1,"2016-11-24":2,"2016-11-18":2,"2016-11-26":1,"2016-11-16":3,"2016-11-27":1,"2016-11-28":1}'}

#json_str = json.dumps(data)
#print(json_str)

#hjson = json.loads(json_str)
#print(hjson['name'])

print(data)
print(data['hasTeachin'])
data_decode = json.loads(data)
print(data_decode)

#hasTeachin