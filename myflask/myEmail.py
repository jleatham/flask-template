from jinja2 import Environment 

def create_email_html(archList):
    htmlTemplate = """

            <table {{ tableStyle }} >
                <tbody>
                    <tr>
                        <td {{ tdStyle }}>
                            <span {{ spanStyleBlue }}>Cisco Enterprise Networking News</span>
                        </td>
                    </tr>
            {% for i in archList %}
            {% if i.category == 'news' %}

                    <tr>
                        <td {{ tdStyle }}>
                            <ul>

                                <li>
                                    <span {{ spanStyle }}> {{ i.bullet }} {% if i.sbLink %}<a href="{{ i.sbLink }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                {% if i.subBullet1 %} 
                                    <ul>
                                        <li>
                                            <span {{ spanStyle }}> {{ i.subBullet1 }}{% if i.sb1Link %} <a href="{{ i.sb1Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>
                                        {% if i.subBullet2 %} 
                                        <li>
                                            <span {{ spanStyle }}> {{ i.subBullet2 }}{% if i.sb2Link %} <a href="{{ i.sb2Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %}
                                        {% if i.subBullet3 %} 
                                        <li>
                                            <span {{ spanStyle }}> {{ i.subBullet3 }}{% if i.sb3Link %} <a href="{{ i.sb3Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %}   
                                        {% if i.subBullet4 %} 
                                        <li>
                                            <span {{ spanStyle }}> {{ i.subBullet4 }}{% if i.sb4Link %} <a href="{{ i.sb4Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                        </li>                                
                                        {% endif %} 
                                        {% if i.subBullet5 %} 
                                        <li>
                                            <span {{ spanStyle }}> {{ i.subBullet5 }}{% if i.sb5Link %} <a href="{{ i.sb5Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
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
        spanStyle =  'style= "color:black;font-family:ciscosans,sans-serif;font-size:12pt;"',
        tableStyle = 'border="0" cellpadding="0" cellspacing="0" style="font-family:-webkit-standard;letter-spacing:normal;orphans:auto;text-indent:0px;text-transform:none;widows:auto;word-spacing:0px;-webkit-text-size-adjust:auto;-webkit-text-stroke-width:0px;text-decoration:none;border-collapse:collapse;"',
        tdStyle = 'style="width:70%;border:1pt solid windowtext;padding:0in 5.4pt;vertical-align:top;"',
        spanStyleBlue = 'style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;"',
        aStyle = 'style="color:rgb(149, 79, 114);text-decoration:underline;"'
    )
    print (htmlMsg)
    return htmlMsg

'''
spanStyle =  'style= "color:black;font-family:ciscosans,sans-serif;font-size:12pt;"'
tableStyle = 'border="0" cellpadding="0" cellspacing="0"'
tdStyle = 'style="width:70%;border:1pt solid windowtext;padding:0in 5.4pt;vertical-align:top;"'
spanStyleBlue = 'style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;"'
aStyle = 'style="color:rgb(149, 79, 114);text-decoration:underline;"'

bullet, bLink,
                subBullet1, sb1Link, subBullet2, sb2Link,
                subBullet3, sb3Link, subBullet4, sb4Link,
                subBullet5, sb5Link


    <table {{ tableStyle }} >
        <tbody>
            <tr>
                <td {{ tdStyle }}>
                    <span {{ spanStyleBlue }}>Cisco Data Center and Cloud News</span>
                </td>
            </tr>
    {{% for i in archList %}}
    {% if i.category == 'news' %}

            <tr>
                <td {{ tdStyle }}>
                    <ul>

                        <li>
                            <span {{ spanStyle }}> {{ i.bullet }} {% if i.sbLink %}<a href="{{ i.sbLink }}" {{ aStyle }}>Link</a>{% endif %}</span>
                        {% if i.subBullet1 %} 
                            <ul>
                                <li>
                                    <span {{ spanStyle }}> {{ i.subBullet1 }}{% if i.sb1Link %} <a href="{{ i.sb1Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                </li>
                                {% if i.subBullet2 %} 
                                <li>
                                    <span {{ spanStyle }}> {{ i.subBullet2 }}{% if i.sb2Link %} <a href="{{ i.sb2Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                </li>                                
                                {% endif %}
                                {% if i.subBullet3 %} 
                                <li>
                                    <span {{ spanStyle }}> {{ i.subBullet3 }}{% if i.sb3Link %} <a href="{{ i.sb3Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                </li>                                
                                {% endif %}   
                                {% if i.subBullet4 %} 
                                <li>
                                    <span {{ spanStyle }}> {{ i.subBullet4 }}{% if i.sb4Link %} <a href="{{ i.sb4Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
                                </li>                                
                                {% endif %} 
                                {% if i.subBullet5 %} 
                                <li>
                                    <span {{ spanStyle }}> {{ i.subBullet5 }}{% if i.sb5Link %} <a href="{{ i.sb5Link }}" {{ aStyle }}>Link</a>{% endif %}</span>
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














<span style="color:black;font-family:ciscosans,sans-serif;font-size:12pt;"></span>
<table border="0" cellpadding="0" cellspacing="0" >
    <tbody>
-Blue header-
        <tr>
            <td style="width:70%;border:1pt solid windowtext;padding:0in 5.4pt;vertical-align:top;">
                <span style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;"></span>
            </td>
        </tr>
-body points
        <tr>
            <td style="width:70%;border:1pt solid windowtext;padding:0in 5.4pt;vertical-align:top;">
                <ul>
    -main bullet, no sub bullet
                    <li>
                        <span style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;">
                            <a href="#" style="color:rgb(149, 79, 114);text-decoration:underline;">Link</a>
                        </span>
                    </li>

    -Main bullet, sub bullets
                    <li>
                        <span style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;">
                            <a href="#" style="color:rgb(149, 79, 114);text-decoration:underline;">Link</a>
                        </span>
                    <ul>
                        <li>
                            <span style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;">
                                <a href="#" style="color:rgb(149, 79, 114);text-decoration:underline;">Link</a>
                            </span>
                        </li>
                    </ul>
                    </li>

                </ul>
                <span style="color:#00b0f0;font-family:ciscosans,sans-serif;font-size:12pt;"></span>
            </td>
            
        </tr>

    </tbody>
</table>





<span style="color:black;font-family:ciscosans,sans-serif;font-size:12pt;">Architecture week by your SE and overlay teams. Thanks to the overlay teams for providing the resources.</span>
<br />
<br />
<b><u><span style="color:black;font-family:ciscosans,sans-serif;font-size:12pt;">Goal:</span></u></b>
<br />
<ul>
  <li>
    <span style="color:black;font-family:ciscosans,sans-serif;font-size:12pt;">Remind the region of sales resources for a specific architecture</span>
  </li>
  <li>
    <span style="color:black;font-family:ciscosans,sans-serif;font-size:12pt;">Take deliberate actions from the sales resources to build pipeline.</span>
  </li>

</ul>


<b><u><span style="color:red;font-family:ciscosans,sans-serif;font-size:12pt;">***************************************Email to customer****************************************************</span></u></b>
<br />



'''