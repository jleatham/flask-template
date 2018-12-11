from jinja2 import Environment 


def create_email_table(archList,category, header):
    htmlTemplate = """

            <table {{ tableStyle }} >
                <tbody {{ tbodyStyle }}>
                    <tr {{ trStyle }}>
                        <td {{ tdStyleHeader }}>
                            <span {{ spanStyleBlue }}>{{ header }}</span>
                        </td>
                    </tr>
            {% for i in archList %}
            {% if i.category == category %}

                    <tr {{ trStyle }}>
                        <td {{ tdStyleBody }}>
                            <ul {{ ulStyle }}>

                                <li {{ liStyle }}>
                                    <span {{ spanStyle }}> {{ i.bullet }} {% if i.sbLink %}  -- <a href="{{ i.sbLink }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                {% if i.subBullet1 %} 
                                    <ul {{ ulStyle }}>
                                        <li {{ liStyle }}>
                                            <span {{ spanStyle }}> {{ i.subBullet1 }}{% if i.sb1Link %}   -- <a href="{{ i.sb1Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>
                                        {% if i.subBullet2 %} 
                                        <li {{ liStyle }}>
                                            <span {{ spanStyle }}> {{ i.subBullet2 }}{% if i.sb2Link %}   -- <a href="{{ i.sb2Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %}
                                        {% if i.subBullet3 %} 
                                        <li {{ liStyle }}>
                                            <span {{ spanStyle }}> {{ i.subBullet3 }}{% if i.sb3Link %}   -- <a href="{{ i.sb3Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %}   
                                        {% if i.subBullet4 %} 
                                        <li {{ liStyle }}>
                                            <span {{ spanStyle }}> {{ i.subBullet4 }}{% if i.sb4Link %}   -- <a href="{{ i.sb4Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %} 
                                        {% if i.subBullet5 %} 
                                        <li {{ liStyle }}>
                                            <span {{ spanStyle }}> {{ i.subBullet5 }}{% if i.sb5Link %}   -- <a href="{{ i.sb5Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %}                                                                                                 
                                    </ul>
                                {% endif %}
                                </li>

                            </ul>
                        </td>
            {% endif %}
            {% endfor %}        
                    </tr>

                </tbody>
            </table>
        """
    htmlMsg = Environment().from_string(htmlTemplate).render(
        archList = archList,
        header = header,
        category = category,
        trStyle = 'style="background-color:transparent;"',
        spanStyle =  'style= "color:black;font-family:ciscosans,sans-serif;font-size:12pt;"',
        tableStyle = 'style="margin:5px;width:70%;border:2pt solid;cellpadding=0;cellspacing=0;border-radius:1px;font-family:-webkit-standard;letter-spacing:normal;orphans:auto;text-indent:0px;text-transform:none;widows:auto;word-spacing:0px;-webkit-text-size-adjust:auto;-webkit-text-stroke-width:0px;text-decoration:none;border-collapse:collapse;"',
        tdStyleHeader = 'style="width:100%;border:1pt solid windowtext;padding:0in 5.4pt;vertical-align:top;"',
        tdStyleBody = 'style="width:100%;border-style:none solid;border-left-width:1pt;border-right-width:1pt;padding:0in 5.4pt;vertical-align:top;"',
        spanStyleBlue = 'style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;"',
        aStyle = 'style="color:rgb(149, 79, 114);text-decoration:underline;"',
        tbodyStyle = 'style=""',
        ulStyle = 'style=""',
        liStyle = 'style=""'
    )
    #print (htmlMsg)
    return htmlMsg

def create_html_msg(archList):
    spacer = add_html_component("spacer")
    divider = add_html_component("divider")
    htmlMsg = ""
    emailTable = create_email_table(archList,'news', 'News')
    htmlMsg = htmlMsg + emailTable + spacer
    emailTable = create_email_table(archList,'demo', 'Demonstrations')
    htmlMsg = htmlMsg + emailTable + spacer
    emailTable = create_email_table(archList,'services', 'Services')
    htmlMsg = htmlMsg + emailTable + spacer + divider + spacer
    emailTable = create_email_table(archList,'ea', 'EA')
    htmlMsg = htmlMsg + emailTable + spacer
    emailTable = create_email_table(archList,'capital', 'Cisco Capital')
    htmlMsg = htmlMsg + emailTable + spacer
    emailTable = create_email_table(archList,'promo', 'Promotions')
    htmlMsg = htmlMsg + emailTable + spacer
    emailTable = create_email_table(archList,'proposal', 'Proposals - Unsolicited BoMs')
    htmlMsg = htmlMsg + emailTable + spacer
    emailTable = create_email_table(archList,'spiff', 'SPIFFs')
    htmlMsg = htmlMsg + emailTable + spacer
    return htmlMsg

def add_html_component(component):
    if component == "spacer":
        htmlComponent = "</br>"
    elif component == "divider":
        htmlComponent = """ <span style= "color:red;font-family:ciscosans,sans-serif;font-size:12pt;">*********************(Internal use only – Don’t send below to customers)*********************</span> """
    return htmlComponent
       