
// 导航栏Logo 
module.exports = {
    base: "/owl/",


    themeConfig: {
        logo: '/logo.png',


        search: true, //禁用搜索栏

        lastUpdated: '最新一次更新时间为：', //显示更新时间

        //nextLinks:false,
        //prevLinks:false, 自动获取 当前页的上一篇和下一篇文章

        smoothScroll: true, //启动页面滚动效果

        //默认下sidebar只显示当前活动页面的标题，但 displayAllHeaders: true 来设置所有页面的标题链接

        sidebar: {
            "/fish/": [
                'fish-a',
                'fish-b',
                {
                    title: 'meat',
                    collapsable: false,
                    children: [
                        '/fish/meat/meat-a',
                        '/fish/meat/meat-b'
                    ]
                },
                {
                    title: 'cat',
                    collaspable: false,
                    children: [
                        '/fish/cat/cat-a',
                        '/fish/cat/cat-b'
                    ]
                }
            ],
            "/up/": [
                'up-a',
                'up-b',

            ]
        }








    }
}
