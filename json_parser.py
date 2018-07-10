import json


def parse():
    j = '''
    [{"type":1,"poemId":27253,"mingcheng":"无题","zuozhe":"李商隐","chaodai":"唐代","zhaiyao":"相见时难别亦难，东风无力百花残。"},{"type":1,"poemId":60957,"mingcheng":"无题·来是空言去绝踪","zuozhe":"李商隐","chaodai":"唐代","zhaiyao":"来是空言去绝踪，月斜楼上五更钟。"},{"type":1,"poemId":24295,"mingcheng":"夜雨寄北","zuozhe":"李商隐","chaodai":"唐代","zhaiyao":"君问归期未有期，巴山夜雨涨秋池。"},{"type":1,"poemId":64251,"mingcheng":"秋思","zuozhe":"陆游","chaodai":"宋代","zhaiyao":"利欲驱人万火牛，江湖浪迹一沙鸥。"},{"type":1,"poemId":27253,"mingcheng":"无题","zuozhe":"李商隐","chaodai":"唐代","zhaiyao":"相见时难别亦难，东风无力百花残。"},{"type":1,"poemId":47671,"mingcheng":"卜算子·我住长江头","zuozhe":"李之仪","chaodai":"宋代","zhaiyao":"我住长江头，君住长江尾。"},{"type":1,"poemId":65327,"mingcheng":"秋声赋","zuozhe":"欧阳修","chaodai":"宋代","zhaiyao":"欧阳子方夜读书，闻有声自西南来者，悚然而听之，曰：“异哉！”初淅沥以萧飒，忽奔腾而砰湃，如波涛夜惊，风雨骤至。"},{"type":1,"poemId":26921,"mingcheng":"幽居冬暮","zuozhe":"李商隐","chaodai":"唐代","zhaiyao":"羽翼摧残日，郊园寂寞时。"},{"type":1,"poemId":61414,"mingcheng":"留别妻","zuozhe":"佚名","chaodai":"两汉","zhaiyao":"结发为夫妻，恩爱两不疑。"},{"type":1,"poemId":64677,"mingcheng":"忆秦娥·花深深","zuozhe":"郑文妻","chaodai":"宋代","zhaiyao":"花深深。"},{"type":2,"poemId":18,"mingcheng":"殷其雷","zuozhe":"佚名","chaodai":"先秦","zhaiyao":"殷其雷，在南山之阳。"},{"type":2,"poemId":14,"mingcheng":"草虫","zuozhe":"佚名","chaodai":"先秦","zhaiyao":"喓喓草虫，趯趯阜螽。"},{"type":2,"poemId":66323,"mingcheng":"谢新恩·樱花落尽阶前月","zuozhe":"李煜","chaodai":"五代","zhaiyao":"樱花落尽阶前月，象床愁倚薰笼。"},{"type":2,"poemId":1134,"mingcheng":"横吹曲辞。幽州胡马客歌","zuozhe":"李白","chaodai":"唐代","zhaiyao":"幽州胡马客，绿眼虎皮冠。"},{"type":2,"poemId":19,"mingcheng":"羔羊","zuozhe":"佚名","chaodai":"先秦","zhaiyao":"羔羊之皮，素丝五紽。"},{"type":2,"poemId":1276,"mingcheng":"相和歌辞。胡无人行","zuozhe":"李白","chaodai":"唐代","zhaiyao":"严风吹霜海草凋，筋干精坚胡马骄。"},{"type":2,"poemId":20,"mingcheng":"小星","zuozhe":"佚名","chaodai":"先秦","zhaiyao":"嘒彼小星，三五在东。"},{"type":3,"poemId":60986,"mingcheng":"赠别","zuozhe":"杜牧","chaodai":"唐代","zhaiyao":"多情却似总无情，唯觉樽前笑不成。"}]
    '''
    new_list = []
    # read json
    text = json.loads(j)
    for t in text:
        new_list.append(t['zhaiyao'])
    # write list to file, use encoding utf-8
    with open('poetry.txt', 'w', encoding='utf-8') as f:
        for i in new_list:
            f.write("%s\n" % i)


if __name__ == '__main__':
    parse()
