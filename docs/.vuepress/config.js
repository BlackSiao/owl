
// 导航栏Logo 
module.exports = {
    base: "/owl/",


    themeConfig: {
        logo: '/back.png',

        //导航栏除了返回首页，还应该想点其他的动能
        navbar: [
            { text: 'Home', link: '/', target: '_self', rel: '' },

        ],

        search: true, //禁用搜索栏
        searchMaxSuggestions: 10,

        lastUpdated: '最新一次更新时间为：', //显示更新时间

        //nextLinks:false,
        //prevLinks:false, 自动获取 当前页的上一篇和下一篇文章

        smoothScroll: true, //启动页面滚动效果

        //默认下sidebar只显示当前活动页面的标题，但 displayAllHeaders: true 来设置所有页面的标题链接
        sidebarDepth: 0,
        sidebar: {
            "/salted_fish/": [
                {
                    title: '来点二次元',
                    path: '/salted_fish/jap/jap_index',
                    collaspable: false,
                    children: [
                        '/salted_fish/jap/来自深渊',
                        '/salted_fish/jap/异世界舅舅'
                    ]

                },
                {
                    title: 'steam游戏推荐',
                    path: '/salted_fish/game/game_index',
                    collaspable: false,                
                    children: [
                        {
                            title: "Civilization",
                            path: "/salted_fish/game/civilization"
                        },
                        {
                            title: "Darkest Dungeon",
                            path: "/salted_fish/game/dungeon"
                        }
                    ]

                },
                {
                    title: '电影',
                    path: '/salted_fish/movie/movie_index',
                    collaspable: false,
                    children: [
                        {
                            title: "李安《父亲三部曲》",
                            path: "/salted_fish/movie/李安"
                        },
                        {
                            title: "《隐入尘烟》",
                            path: "/salted_fish/movie/隐入尘烟"
                        },
                        {
                            title: "《西线无战事》",
                            path: "/salted_fish/movie/西线无战事"
                            
                        }

                    ]
                    
                }
            ],
            "/rise_up/": [
                {
                    title: 'C++',
                    path: '/rise_up/C++'
                },
                {
                    title: '计算机网络',
                    path: '/rise_up/网络原理'
                }
                

            ]
        }








    }
}
