# Functions that return HTML code :


def docstr(nullstr=""):
    return "<!DOCTYPE html>\n"


def metastr(charset="utf-8"):
    return '<meta charset="' + charset + '">\n'


def html(string=""):
    return "<html>\n" + string + "</html>"


def head(string=""):
    return "<head>\n" + string + "</head>\n"


def title(string=""):
    return "<title>" + string + "</title>\n"


def style(string=""):
    return "<style>\n" + string + "\n</style>\n"


def body(string=""):
    return "<body>\n" + string + "</body>\n"


def h1(string="Headline 1"):
    return "<h1>" + string + "</h1>\n"


def h2(string="Headline 2"):
    return "<h2>" + string + "</h2>\n"


def h3(string="Headline 3"):
    return "<h3>" + string + "</h3>\n"


def h4(string="Headline 4"):
    return "<h4>" + string + "</h4>\n"


def h5(string="Headline 5"):
    return "<h5>" + string + "</h5>\n"


def h6(string="Headline 6"):
    return "<h6>" + string + "</h6>\n"


def addscript(script=""):
    return "<script>\n" + script + "\n</script>\n"


def button(idstr="", label=""):
    return '<button id="' + idstr + '">' + label + '</button>\n'


def imgin(imgsrc=""):
    return '<img src="' + imgsrc + '"/>'


def linkin(link="", string=""):
    return '<a href="' + link + '">\n' + string + '</a>\n'


def bulletlist(string=""):
    return "<ul>\n" + string + "</ul>\n"


def numlist(string=""):
    return "<ol>\n" + string + "</ol>\n"


def listitem(string=""):
    return "<li>" + string + "</li>\n"


def para(string=""):
    return "<p>\n" + string.replace("\n", "<br>\n") + "\n</p>\n"


def bold(string=""):
    return "<strong>" + string + "</strong>"


def italic(string=""):
    return "<em>" + string + "</em>"


def maketable(string=""):
    return "<table>\n" + string + "</table>\n"


def tablerow(string=""):
    return "<tr>\n" + string + "</tr>\n"


def tablehead(string=""):
    return "<th>" + string + "</th>\n"


def tabledata(string=""):
    return "<td>" + string + "</td>\n"

# Function to create html file using python syntax with this module :


def htout(htstr="", filename="output", extension=".html"):
    with open(filename + extension, "w") as htfile:
        htfile.write(htstr)


# Sample HTML for syntax documentation :
'''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>HTML Sample</title>
        <style>
            h1 {
                color: red;
            }
        </style>
    </head>
    <body>
        <h1>Headline 1</h1>
        <h2>Headline 2</h2>
        <p>
        Paragraph lines...
        continued...
        <strong>continued in bold</strong>...
        <em>continued in italic</em>...
        ended.
        </p>
        <ul>
            <li>list item 1</li>
            <li>list item 2</li>
        </ul>
        <ol>
            <li>list item 1</li>
            <li>list item 2</li>
        </ol>
        <table>
            <tr>
                <th>Column A</th>
                <th>Column B</th>
            </tr>
            <tr>
                <td>Item A</td>
                <td>Item B</td>
            </tr>
        </table>
    </body>
</html>
'''

# Code to print the HTML above :

if __name__ == "__main__":
    content = str(
        docstr() +
        html(
            head(
                metastr(charset="utf-8") +
                title("HTML Sample") +
                style("h1 {\ncolor: red;\n}")
            ) +
            body(
                h1("Headline 1") +
                h2("Headline 2") +
                para("Paragraph lines...\ncontinued...\nended.") +
                bulletlist(
                    listitem("list item 1") +
                    listitem("list item 2")
                ) +
                numlist(
                    listitem("list item 1") +
                    listitem("list item 2")
                ) +
                maketable(
                    tablerow(
                        tablehead("Column A") + tablehead("Column B")
                    ) +
                    tablerow(
                        tabledata("Item A") + tabledata("Item B")
                    )
                )
            )
        )
    )
    print(content)
