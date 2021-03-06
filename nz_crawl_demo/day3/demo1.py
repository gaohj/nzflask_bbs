from lxml import etree

text = """
<ul class="item_con_list" style="display: block;">

    <li class="con_list_item first_row default_list" data-index="0" data-positionid="3580958" data-salary="18k-25k" data-company="众禄金融" data-positionname="python工程师" data-companyid="50285" data-hrid="1509336" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3580958.html" target="_blank" data-index="0" data-lg-tj-id="8E00" data-lg-tj-no="


                    0101


                " data-lg-tj-cid="3580958" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">python工程师</h3>




                                        <span class="add">[<em>罗湖区</em>]</span>





                    </a>
                    <span class="format-time">3天前发布</span>




















                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="石经理">
                            <input type="hidden" class="hr_position" value="招聘经理">
                            <input type="hidden" class="target_hr" value="1509336">
                            <input type="hidden" class="target_position" value="3580958">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0101" data-lg-tj-cid="50285" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>













                <i class="pos_icon pos_icon_12"></i></div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">18k-25k</span>
                        <!--<i></i>-->经验3-5年 / 大专
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/50285.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0101


                " data-lg-tj-cid="50285" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">众禄金融</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,金融 / 上市公司
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/50285.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0101


                " data-lg-tj-cid="50285" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image2/M00/18/65/CgotOVn65YSAAu7lAAAVwDCKc5w606.png" alt="众禄金融" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>金融</span>

                        <span>信息安全</span>

                        <span>php</span>

                        <span>Java</span>

                        <span>web</span>

                </div>

            <div class="li_b_r">“互联网金融,高速发展,五险一金,金融中心”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="1" data-positionid="3172437" data-salary="10k-15k" data-company="乐易网络" data-positionname="python开发工程师" data-companyid="33627" data-hrid="569371" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3172437.html" target="_blank" data-index="1" data-lg-tj-id="8E00" data-lg-tj-no="


                    0102


                " data-lg-tj-cid="3172437" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">python开发工程师</h3>




                                        <span class="add">[<em>南山区</em>]</span>





                    </a>
                    <span class="format-time">2天前发布</span>
















                            <input type="hidden" class="hr_portrait" value="i/image/M00/4C/88/CgpFT1lwWhiAB5C2AAD55Ttkxck626.jpg">
                            <input type="hidden" class="hr_name" value="Tina">
                            <input type="hidden" class="hr_position" value="HR">
                            <input type="hidden" class="target_hr" value="569371">
                            <input type="hidden" class="target_position" value="3172437">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0102" data-lg-tj-cid="33627" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1">
	<div class="chat_pop_up">
		<span class="arrow"></span>
		<dl class="chat_main clearfix">
			<dt><div class="chat_qrcode"><canvas width="116" height="116"></canvas></div></dt>
			<dd>
				<dl class="chat_head clearfix">
					<dt>

							<img class="hr_headpic" src="https://static.lagou.com/i/image/M00/4C/88/CgpFT1lwWhiAB5C2AAD55Ttkxck626.jpg" alt="hr头像" width="62" height="62">

					</dt>
					<dd>
						<div class="hr_name">Tina</div>
						<div class="hr_position">HR</div>
					</dd>
					<dd class="tips_text">Hi，对我发布的职位感兴趣？用拉勾APP扫码，直接和我聊聊吧！</dd>
				</dl>
			</dd>
		</dl>
	</div>

</div>

















                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-15k</span>
                        <!--<i></i>-->经验3-5年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/33627.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0102


                " data-lg-tj-cid="33627" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">乐易网络</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,游戏 / A轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/33627.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0102


                " data-lg-tj-cid="33627" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/57/05/CgqKkVfOIv6AQwyPAAEg94dso0Q147.png" alt="乐易网络" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>php</span>

                        <span>MySQL</span>

                        <span>后端</span>

                </div>

            <div class="li_b_r">“五险一金,年终奖金”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="2" data-positionid="3088129" data-salary="10k-20k" data-company="对酒当歌" data-positionname="python开发工程师" data-companyid="32901" data-hrid="557623" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3088129.html" target="_blank" data-index="2" data-lg-tj-id="8E00" data-lg-tj-no="


                    0103


                " data-lg-tj-cid="3088129" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">python开发工程师</h3>




                                        <span class="add">[<em>宝安区</em>]</span>





                    </a>
                    <span class="format-time">2天前发布</span>












                            <input type="hidden" class="hr_portrait" value="i/image2/M00/1D/93/CgoB5loJToSAXS5UAAAxRCAgR0I656.jpg">
                            <input type="hidden" class="hr_name" value="Fiona">
                            <input type="hidden" class="hr_position" value="HR">
                            <input type="hidden" class="target_hr" value="557623">
                            <input type="hidden" class="target_position" value="3088129">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0103" data-lg-tj-cid="32901" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>





















                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-20k</span>
                        <!--<i></i>-->经验1-3年 / 大专
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/32901.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0103


                " data-lg-tj-cid="32901" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">对酒当歌</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    电子商务,O2O / A轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/32901.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0103


                " data-lg-tj-cid="32901" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image2/M00/1D/93/CgoB5loJTs6AbgL2AAAxM5rVkG8611.jpg" alt="对酒当歌" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>php</span>

                        <span>Java</span>

                        <span>MySQL</span>

                </div>

            <div class="li_b_r">“五险一金,免费班车”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="3" data-positionid="3163697" data-salary="15k-30k" data-company="笨鸟社交" data-positionname="python工程师" data-companyid="84086" data-hrid="3628930" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3163697.html" target="_blank" data-index="3" data-lg-tj-id="8E00" data-lg-tj-no="


                    0104


                " data-lg-tj-cid="3163697" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">python工程师</h3>




                                        <span class="add">[<em>南山区</em>]</span>





                    </a>
                    <span class="format-time">1天前发布</span>














                            <input type="hidden" class="hr_portrait" value="i/image2/M00/21/C0/CgotOVoTm-KAL5xbAAEYJ1YAVhc922.jpg">
                            <input type="hidden" class="hr_name" value="马小姐">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="3628930">
                            <input type="hidden" class="target_position" value="3163697">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0104" data-lg-tj-cid="84086" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>



















                <i class="pos_icon pos_icon_12"></i></div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-30k</span>
                        <!--<i></i>-->经验不限 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/84086.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0104


                " data-lg-tj-cid="84086" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">笨鸟社交</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    企业服务 / B轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/84086.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0104


                " data-lg-tj-cid="84086" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/10/1C/CgpFT1jwK86AVr_OAACaAuJFFLw446.png" alt="笨鸟社交" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>爬虫</span>

                        <span>后端</span>

                        <span>初级</span>

                        <span>中级</span>

                        <span>搜索</span>

                </div>

            <div class="li_b_r">“海量数据”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="4" data-positionid="3867111" data-salary="15k-28k" data-company="博奥特科技" data-positionname="Python工程师" data-companyid="69152" data-hrid="9207315" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3867111.html" target="_blank" data-index="4" data-lg-tj-id="8E00" data-lg-tj-no="


                    0105


                " data-lg-tj-cid="3867111" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python工程师</h3>



                                    <span class="add">[<em>上步</em>]</span>




                    </a>
                    <span class="format-time">2天前发布</span>






























                            <input type="hidden" class="hr_portrait" value="i/image2/M00/1C/84/CgoB5loFXcaAMM23AABudjCbyWs865.png">
                            <input type="hidden" class="hr_name" value="qiuff">
                            <input type="hidden" class="hr_position" value="招聘部">
                            <input type="hidden" class="target_hr" value="9207315">
                            <input type="hidden" class="target_position" value="3867111">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0105" data-lg-tj-cid="69152" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>



                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-28k</span>
                        <!--<i></i>-->经验3-5年 / 大专
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/69152.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0105


                " data-lg-tj-cid="69152" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">博奥特科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,金融 / 未融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/69152.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0105


                " data-lg-tj-cid="69152" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image2/M00/18/B4/CgoB5ln71t2ADbc3AABFDELpI7U021.jpg" alt="博奥特科技" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>金融</span>

                        <span>Java</span>

                        <span>cobol</span>

                </div>

            <div class="li_b_r">“发展前景好,双休,互联网金融”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="5" data-positionid="2889252" data-salary="15k-30k" data-company="万科物业" data-positionname="Python开发工程师" data-companyid="8350" data-hrid="7279982" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/2889252.html" target="_blank" data-index="5" data-lg-tj-id="8E00" data-lg-tj-no="


                    0106


                " data-lg-tj-cid="2889252" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python开发工程师</h3>



                                    <span class="add">[<em>上梅林</em>]</span>




                    </a>
                    <span class="format-time">2天前发布</span>










                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="xiongx04">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="7279982">
                            <input type="hidden" class="target_position" value="2889252">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0106" data-lg-tj-cid="8350" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>























                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-30k</span>
                        <!--<i></i>-->经验3-5年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/8350.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0106


                " data-lg-tj-cid="8350" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">万科物业</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    O2O,生活服务 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/8350.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0106


                " data-lg-tj-cid="8350" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/image2/M00/08/03/CgqLKVYBEtqAD2vhAAARnNY0kzg058.png" alt="万科物业" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>资深</span>

                        <span>高级</span>

                        <span>中级</span>

                        <span>后端开发</span>

                        <span>redis</span>

                </div>

            <div class="li_b_r">“平台好,空间大”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="6" data-positionid="2786718" data-salary="10k-15k" data-company="环球易购" data-positionname="高级python开发工程师" data-companyid="83025" data-hrid="2117758" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/2786718.html" target="_blank" data-index="6" data-lg-tj-id="8E00" data-lg-tj-no="


                    0107


                " data-lg-tj-cid="2786718" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">高级python开发工程师</h3>




                                        <span class="add">[<em>南山区</em>]</span>





                    </a>
                    <span class="format-time">1天前发布</span>








                            <input type="hidden" class="hr_portrait" value="i/image2/M00/1E/F1/CgoB5loL-aGASIqDAAATxYblCtQ334.jpg">
                            <input type="hidden" class="hr_name" value="Hipson">
                            <input type="hidden" class="hr_position" value="首席神秘官">
                            <input type="hidden" class="target_hr" value="2117758">
                            <input type="hidden" class="target_position" value="2786718">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0107" data-lg-tj-cid="83025" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>

























                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">10k-15k</span>
                        <!--<i></i>-->经验3-5年 / 大专
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/83025.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0107


                " data-lg-tj-cid="83025" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">环球易购</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    电子商务 / 上市公司
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/83025.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0107


                " data-lg-tj-cid="83025" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/image1/M00/38/9F/CgYXBlWmIt6Af8k5AABvK21LZWM490.jpg?cc=0.211507520172745" alt="环球易购" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>软件开发</span>

                </div>

            <div class="li_b_r">“上市公司 公司规模大 发展机会多”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="7" data-positionid="3325916" data-salary="15k-23k" data-company="晶泰科技" data-positionname="高级Python开发工程师" data-companyid="76066" data-hrid="5281055" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3325916.html" target="_blank" data-index="7" data-lg-tj-id="8E00" data-lg-tj-no="


                    0108


                " data-lg-tj-cid="3325916" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">高级Python开发工程师</h3>



                                    <span class="add">[<em>香蜜湖</em>]</span>




                    </a>
                    <span class="format-time">2天前发布</span>


















                            <input type="hidden" class="hr_portrait" value="i/image/M00/48/46/CgpFT1loITKAe1YZAAD7YMAGvnI602.jpg">
                            <input type="hidden" class="hr_name" value="李丹慧">
                            <input type="hidden" class="hr_position" value="HR经理">
                            <input type="hidden" class="target_hr" value="5281055">
                            <input type="hidden" class="target_position" value="3325916">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0108" data-lg-tj-cid="76066" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>















                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-23k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/76066.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0108


                " data-lg-tj-cid="76066" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">晶泰科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    企业服务,医疗健康 / B轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/76066.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0108


                " data-lg-tj-cid="76066" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/46/CE/CgqKkVeNuE-AMgmGAACJzPxVN30374.jpg" alt="晶泰科技" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>云计算</span>

                        <span>后端开发</span>

                        <span>web</span>

                        <span>Go</span>

                        <span>django</span>

                </div>

            <div class="li_b_r">“大牛多,公司氛围好,周末双休,成长快”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="8" data-positionid="3727987" data-salary="14k-20k" data-company="盖威" data-positionname="Python开发工程师" data-companyid="3956" data-hrid="5713991" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3727987.html" target="_blank" data-index="8" data-lg-tj-id="8E00" data-lg-tj-no="


                    0109


                " data-lg-tj-cid="3727987" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python开发工程师</h3>



                                    <span class="add">[<em>科技园</em>]</span>




                    </a>
                    <span class="format-time">3天前发布</span>






















                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="hr-gw">
                            <input type="hidden" class="hr_position" value="HR经理">
                            <input type="hidden" class="target_hr" value="5713991">
                            <input type="hidden" class="target_position" value="3727987">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0109" data-lg-tj-cid="3956" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>











                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">14k-20k</span>
                        <!--<i></i>-->经验3-5年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/3956.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0109


                " data-lg-tj-cid="3956" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">盖威</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    金融 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/3956.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0109


                " data-lg-tj-cid="3956" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/image1/M00/00/0A/Cgo8PFTUWBWAJ-eQAAA1pEtnnYo973.png" alt="盖威" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>linux</span>

                        <span>C++</span>

                </div>

            <div class="li_b_r">“福利待遇好”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="9" data-positionid="2010228" data-salary="15k-25k" data-company="极光" data-positionname="高级Python开发工程师" data-companyid="917" data-hrid="2153176" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/2010228.html" target="_blank" data-index="9" data-lg-tj-id="8E00" data-lg-tj-no="


                    0110


                " data-lg-tj-cid="2010228" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">高级Python开发工程师</h3>



                                    <span class="add">[<em>南头</em>]</span>




                    </a>
                    <span class="format-time">2天前发布</span>


                            <input type="hidden" class="hr_portrait" value="i/image2/M00/0A/38/CgotOVncPOGAR2E7AABUArhVY0U298.jpg">
                            <input type="hidden" class="hr_name" value="Maggie">
                            <input type="hidden" class="hr_position" value="HRBP">
                            <input type="hidden" class="target_hr" value="2153176">
                            <input type="hidden" class="target_position" value="2010228">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0110" data-lg-tj-cid="917" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>































                <i class="pos_icon pos_icon_12"></i></div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-25k</span>
                        <!--<i></i>-->经验3-5年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/917.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0110


                " data-lg-tj-cid="917" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">极光</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,数据服务 / D轮及以上
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/917.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0110


                " data-lg-tj-cid="917" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/37/20/CgqKkVdfms6Ac6dNAABY3gBvuqI944.jpg" alt="极光" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>云计算</span>

                        <span>linux</span>

                        <span>云平台</span>

                        <span>django</span>

                </div>

            <div class="li_b_r">“五险一金、14薪/年、下午茶、工作餐等等”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="10" data-positionid="2022151" data-salary="20k-35k" data-company="航仕科技" data-positionname="Python开发" data-companyid="129877" data-hrid="5095526" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/2022151.html" target="_blank" data-index="10" data-lg-tj-id="8E00" data-lg-tj-no="


                    0111


                " data-lg-tj-cid="2022151" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python开发</h3>



                                    <span class="add">[<em>科技园</em>]</span>




                    </a>
                    <span class="format-time">2017-11-21</span>




                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="hr">
                            <input type="hidden" class="hr_position" value="高级招聘经理">
                            <input type="hidden" class="target_hr" value="5095526">
                            <input type="hidden" class="target_position" value="2022151">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0111" data-lg-tj-cid="129877" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>





























                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">20k-35k</span>
                        <!--<i></i>-->经验3-5年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/129877.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0111


                " data-lg-tj-cid="129877" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">航仕科技</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网,O2O / C轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/129877.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0111


                " data-lg-tj-cid="129877" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/2C/9A/Cgp3O1c5oTuAVfXXAABDG8Kg38w820.jpg" alt="航仕科技" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">


                            <span>年底双薪</span>



                            <span>午餐补助</span>



                            <span>专项奖金</span>



                            <span>绩效奖金</span>


                </div>

            <div class="li_b_r">“BAT的薪资福利待遇，更有技术大牛传授技术”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="11" data-positionid="3759498" data-salary="15k-30k" data-company="Minieye" data-positionname="python工程师" data-companyid="124262" data-hrid="4784940" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3759498.html" target="_blank" data-index="11" data-lg-tj-id="8E00" data-lg-tj-no="


                    0112


                " data-lg-tj-cid="3759498" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">python工程师</h3>




                                        <span class="add">[<em>南山区</em>]</span>





                    </a>
                    <span class="format-time">12:39发布</span>
























                            <input type="hidden" class="hr_portrait" value="i/image/M00/6C/B8/CgpEMlmtQ92AOPnVAACbmIFfngQ360.jpg">
                            <input type="hidden" class="hr_name" value="HRM">
                            <input type="hidden" class="hr_position" value="">
                            <input type="hidden" class="target_hr" value="4784940">
                            <input type="hidden" class="target_position" value="3759498">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0112" data-lg-tj-cid="124262" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>









                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-30k</span>
                        <!--<i></i>-->经验1-3年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/124262.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0112


                " data-lg-tj-cid="124262" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">Minieye</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    硬件,其他 / A轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/124262.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0112


                " data-lg-tj-cid="124262" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/B1/8D/CgqKkVi5Jd6AA65GAAAmAaWjB9U423.png" alt="Minieye" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">


                            <span>无人驾驶</span>



                            <span>国际标准</span>



                            <span>车厂合作</span>



                            <span>海归团队</span>


                </div>

            <div class="li_b_r">“无人驾驶,车厂合作,扁平化管理,股票期权”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="12" data-positionid="2268991" data-salary="15k-30k" data-company="糗事百科" data-positionname="Python" data-companyid="1015" data-hrid="94398" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/2268991.html" target="_blank" data-index="12" data-lg-tj-id="8E00" data-lg-tj-no="


                    0113


                " data-lg-tj-cid="2268991" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python</h3>



                                    <span class="add">[<em>科技园</em>]</span>




                    </a>
                    <span class="format-time">2天前发布</span>






                            <input type="hidden" class="hr_portrait" value="image1/M00/1C/89/Cgo8PFUmLZ-AJRIkAAAgw3YTWBk532.png">
                            <input type="hidden" class="hr_name" value="糗百招聘">
                            <input type="hidden" class="hr_position" value="招聘HR">
                            <input type="hidden" class="target_hr" value="94398">
                            <input type="hidden" class="target_position" value="2268991">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0113" data-lg-tj-cid="1015" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>



























                <i class="pos_icon pos_icon_12"></i></div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-30k</span>
                        <!--<i></i>-->经验3-5年 / 本科
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/1015.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0113


                " data-lg-tj-cid="1015" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">糗事百科</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    移动互联网 / A轮
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/1015.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0113


                " data-lg-tj-cid="1015" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/image1/M00/00/05/CgYXBlTUWAGAY0KwAABsvAoi2t4880.png" alt="糗事百科" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>文化娱乐</span>

                </div>

            <div class="li_b_r">“老司机来开车”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="13" data-positionid="3834269" data-salary="15k-25k" data-company="通力互联" data-positionname="Python开发工程师" data-companyid="123777" data-hrid="4752170" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3834269.html" target="_blank" data-index="13" data-lg-tj-id="8E00" data-lg-tj-no="


                    0114


                " data-lg-tj-cid="3834269" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python开发工程师</h3>



                                    <span class="add">[<em>草埔</em>]</span>




                    </a>
                    <span class="format-time">1天前发布</span>


























                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="李龙辉">
                            <input type="hidden" class="hr_position" value="招聘经理">
                            <input type="hidden" class="target_hr" value="4752170">
                            <input type="hidden" class="target_position" value="3834269">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0114" data-lg-tj-cid="123777" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>







                </div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">15k-25k</span>
                        <!--<i></i>-->经验5-10年 / 大专
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/123777.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0114


                " data-lg-tj-cid="123777" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">通力互联</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    电子商务,企业服务 / 不需要融资
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/123777.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0114


                " data-lg-tj-cid="123777" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/i/image/M00/2E/03/CgqKkVc9jmCAI8DpAAD09YLPnBk157.png" alt="通力互联" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>云计算</span>

                        <span>Java</span>

                        <span>SVN</span>

                </div>

            <div class="li_b_r">“高薪高福利”</div>
        </div>
    </li>



    <li class="con_list_item default_list" data-index="14" data-positionid="3836101" data-salary="12k-18k" data-company="金证股份" data-positionname="Python开发" data-companyid="25317" data-hrid="5715150" data-tpladword="0">

        <div class="list_item_top">
            <div class="position">
                <div class="p_top">
                    <a class="position_link" href="https://www.lagou.com/jobs/3836101.html" target="_blank" data-index="14" data-lg-tj-id="8E00" data-lg-tj-no="


                    0115


                " data-lg-tj-cid="3836101" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">
                        <h3 style="max-width: 180px;">Python开发</h3>




                                        <span class="add">[<em>福田区</em>]</span>





                    </a>
                    <span class="format-time">2天前发布</span>




























                            <input type="hidden" class="hr_portrait" value="">
                            <input type="hidden" class="hr_name" value="lis">
                            <input type="hidden" class="hr_position" value="运营总监">
                            <input type="hidden" class="target_hr" value="5715150">
                            <input type="hidden" class="target_position" value="3836101">

                            <div class="chat_me" data-lg-tj-id="1WI0" data-lg-tj-no="0115" data-lg-tj-cid="25317" data-lg-tj-track-code="search_code" data-lg-tj-track-type="1"></div>





                <i class="pos_icon pos_icon_12"></i></div>
                <div class="p_bot">
                    <div class="li_b_l">
                        <span class="money">12k-18k</span>
                        <!--<i></i>-->经验3-5年 / 大专
                    </div>
                </div>
            </div>
            <div class="company">
                <div class="company_name">
                    <a href="https://www.lagou.com/gongsi/25317.html" target="_blank" data-lg-tj-id="8F00" data-lg-tj-no="


                    0115


                " data-lg-tj-cid="25317" data-lg-tj-abt="dm-csearch-useUserAllInterest|0">金证股份</a><i class="company_mark"><span>该企业已上传营业执照并通过资质验证审核</span></i>
                </div>
                <div class="industry">
                    金融 / 上市公司
                </div>
            </div>
            <div class="com_logo">
                <a href="https://www.lagou.com/gongsi/25317.html" target="_blank" data-lg-tj-id="8G00" data-lg-tj-no="


                    0115


                " data-lg-tj-cid="25317" data-lg-tj-abt="dm-csearch-useUserAllInterest|0"><img src="//static.lagou.com/thumbnail_120x120/image1/M00/00/34/Cgo8PFTUXJOAMEEpAAAroeFn454603.jpg" alt="金证股份" width="60" height="60"></a>
            </div>
        </div>
        <div class="list_item_bot">

                <div class="li_b_l">

                        <span>统计</span>

                        <span>财经</span>

                        <span>Perl</span>

                        <span>自然语言处理</span>

                </div>

            <div class="li_b_r">“上市公司,大型项目,年度调薪,薪资福利好”</div>
        </div>
    </li>
    </ul>
"""

html = etree.HTML(text) #将字符串解析为HTML文档

#序列化 HTML文档 
result = etree.tostring(html)
print(result)
