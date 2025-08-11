import random, string, os

charset = 'abcdefghijklmnopqrstuvwxyz, .'
charset_length = len(charset)
max_page_content_length = 3200
max_walls = 4
max_shelves = 5
max_volumes = 32
max_pages = 410
wall = str(random.randint(1, max_walls))
shelf = str(random.randint(1, max_shelves))
volume = str(random.randint(1, max_volumes)).zfill(2)
page = str(random.randint(1, max_pages)).zfill(3)
library_coordinate = int(page + volume + shelf + wall)
hexagon_base = 36

def searchByContent(text, library_coordinate):
    text = ''.join([c for c in text.lower() if c in charset])
    text = text.rstrip().ljust(max_page_content_length, ' ')
    sum_value = 0
    for i, c in enumerate(text[::-1]):
        char_value = ord(c) - ord('a') if c.isalpha() else 28 if c == '.' else 27
        sum_value += char_value * (charset_length**i)

    result = library_coordinate * (charset_length**max_page_content_length) + sum_value
    result = convertToBase(result, hexagon_base)
    return result

def searchByAddress(address):
    hexagon_address, wall, shelf, volume, page = address.split(':')
    volume = volume.zfill(2)
    page = page.zfill(3)
    library_coordinate = int(page + volume + shelf + wall)

    seed = int(hexagon_address, hexagon_base) - library_coordinate * (charset_length**max_page_content_length)
    hexagon_base_result = convertToBase(seed, hexagon_base)
    result = convertToBase(int(hexagon_base_result, hexagon_base), charset_length)

    if len(result) < max_page_content_length:
        random.seed(result)
        while len(result) < max_page_content_length:
            result += charset[int(random.random() * len(charset))]
    elif len(result) > max_page_content_length:
        result = result[-max_page_content_length:]
    return result

def convertToBase(x, base):
    if base == 36: digs = string.digits + 'abcdefghijklmnopqrstuvwxyz'
    elif base == 10: digs = '0123456789'
    elif base == 60: digs = '0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    else: digs = charset

    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1

    x *= sign
    chars = []
    while x:
        chars.append(digs[x % base])
        x //= base
    if sign < 0:
        chars.append('-')
    chars.reverse()
    return ''.join(chars)


#Page content to hexagon address example
search_term = 'lorem ipsum dolor sit amet'
hexagon_address = searchByContent(search_term, library_coordinate)
total_address = hexagon_address + ':' + wall + ':' + shelf + ':' + volume + ':' + page
print("Hexagon address:", total_address)

#Hexagon address to page content example
example_address = '1zdm64iv7p8hniu6lkinbh45asckcgw1nq6e06f2oko5x2wjo4w6lc4q857vizebwh616292qjecuqke0sasybtiqdyxckzysv6053g8cb65ixtrbn5fkq5px0t3ralo9mquu0ferj70ou4d59g6tmthwg4ww044nhwh473pr7o4r8jzl4djaou9dfds14j0tanrv1jaybksm5ufm4xatt43l2ybf2j29amreljd8ntz7enr0z7tdqd4iobda7n5j13c3rww9u4fzlab48ltuk5zofwql2ihp9lvpieifqqhoku7ttvkyb0meru3p9tk1ksxfb0x7pph5k0f2kt554qad4mmzg9nx4nhwnhb1c2bj3eji21x18o1gqyn1fexuk45h3p0b3zsqqkh7a8h9qcmb84rexakwlgjvk0xzqbi8yvbnabi8btllarkvmr3srorfkjhh9w9br3a0teay9l1wkuk6w0d4rukjhfqksqpmf3u6ec01d1yn8ahe8nw6euxly4ttg8iqyi8r1ixklypfmus5d1y68jeo3cv7but33s8kx9w434qgvls5ikjynfu467xdud8pltjih1w833n5stwegn5pgume3bp8v9c4v3r4nnjok3pwx9t193waowhbeavvgkchuyzhegznhnjiddpdm2gzp2ytx0zcsxjc2v650m8bl818rcfhbbwtewskfxsn1l5fhoh8tpjrcf1t3y2ke175p9jg05cjaruj8i6l3w0mhant98oo3ihuxiinjglbz2fitt4ft9a9hnkcw97wjwibd48tzozsw305f4rz7yfno0s03bt8kr5gnz1jgjfhyz1ftw0o3j94pxd93tuk42oi78874e3kx2y3tvdmnpibe5ohs86w1plppwqa9dyi3l7xf80gdp06y1woj98n05tk2nbil602b0vdkytdrn56ykx6ku2t4xkxfcaz7cy3r4gu8482c0bsrlhiq5fz19hgt4se1gws2lgfl889bch5g2vyf3r61tk2v7fn9eh69yjqu019ok4qb4iyl5ti8ldh4r2tp3x7stznvszaoxwxl9bnwl2i1u39mjnpojjjcznon3mubi5igov7w00mra0dtt5jkozun68eosgdvmmdjc2pqihno33ua8incgfzhl4pzge9g6gj4l4vdggry62tlej9khcah7t7d7niwoj6fo7660v52n71ou5mlqqddewwpe1vxp7bmydq7o2hva3s2nyr583kgnbtdwto2xvloz2q51git55vi9qb55i3szj4ypwb235ol4entt797iq6148l27nuiuczf8dlu96igsx766vik1tkf30y9de9338tk92srxjy5ukk0pe2vi08lyvqvt02lkl03jx7wzcku8swul3hu76v3tgm3t4vkzrcnpr0hf6luyoja537mmtjxecm3uv6lqz6qsgw0mdi6mb2adgklda23nfz9eiq51x043slxz9j7yu6gvbg4uftgbow7dk2ji8t2nyuezcdsw3ev6f8so4ohnpvz7c2xe2xo82i0gpgnpeeeyle7ordbllqijwjb8e9tlt8l346707kowgp10u7emhjya8hf7p0rum1q33wzvyr3kntbvxchphug7ry5rl192yrjl0erhkdbfbrfo3chn3yk5rusoe68q69lj07lix8b6h65jr97ouyzz2rtt53syboaxxq7owwokncxtn7yjjvl2uemlvynxk1pnff70zbg1rmvmd4czxk669k0wnvo8xag3xp3osaukw7sise1v1nrwwtiguicjx9ljsh6dickn6n7fyucm0ikpvf36n2dafr9rcgpfz1emsmdaq6jgnhbcjm8f53c4wzdukelwyd8lrri8cvpzf88tffrj6lqxt7ovnop36ydr5hci6kv8j28759xyo4yhlrweqsqpolak1h6hscua4bz6pf8e8xv4koomlswqds5giypgsgm9lfk9hjf5mhdm8q983e76njycciu0rucw1yot71o4l287b4pni646b186eya8h4fxt3g8kyjaqfn3kao36w80rd6zwldxtb4dnxtdi8c3nc5foo82dsa9y8p53xgyvg6pn7spksk6eeufq3ih25v02rhhjpx6xchg88rtwaimzxp7n0rmy9bdwxbicu3kr0nquvabujb12y1s3i5lq2gh885y3g2uco50v1235oz65jm0i8z4lobce3gcrxr63fdqe3wc5c2tg5xxt5bqin7yq8xak01smuo74gm0wihd01yvvdh1f0mqu8abizegn7253nbypnh0pib9b7qcutqwqjd2rrdk9kbbj053hgmer3c46t5ccqrzh61r93npfw1e5z90wb4m149n6gn04xj9o7nwuazfopo8c2o1j2dcmi1g3ja11z8p3uyjkqaykkkccpaasyknhmx9kez2iv803re49nv36d2t8y9t1qt03bmsy3jy1ah8o6mf56gtvmup6gum3og07wph3spt796rjp0aq1rbjx7c8i7gw257sw45cw27qe5u6n4nz09jji3iyevufhbhuwuir5mgtcq38cw9o35aq2ihkmun8p3nvztgbsd8oyuckh5b573ieap1iwhc45v5jui5eyu3anl7nmypujxwjr57re2ecsp72bipaxrw0132vdz6jz5pbcxxslqixxexvldxbwu7s4ox9i56r1j3lcz2tkw0lakadnmwjud7mlobz73y91kqfvuvxzbs1uxxu941oz69888547ox4w3k64w7v3lhaxinr5jod27fhe0ju6krp6jsc7kwfj7byt617m05rzjxmnv8cl10ec6ybwobozer1n4xyyg83zlbk8vsa1nruoz91lsptdsr0aife0v1m99je2l0checgeec759xf6wo1fazt7thkb3snzuxkenlttgw96b0qka00g8zm2hd9qxy23ekkujcdr3k5iykz38bf040nfcdea55rmou3cz1sl5tna64x848gnp95nar6mg2uvrit61bz57tldjysi13vjhwqn6mln43x9guj0894us6nxou27l5bxora5q08vqrzm1hgpzy7ez90w8n12ohe4dz4i7mrnd6qvakuqs0g8gfvqtl09dzkkmvtlsn6ghlcyjt9qmgkn2cxswomuaz8fuuq4q2xi6txbipshyi4wteo0x0jbgemn6h502x67dqnzsoanjmbxy1sq4aoqoo1eo7b1kj2b4zcsm'
contentByAddress = searchByAddress(total_address)
print("Page content:", contentByAddress.rstrip())
