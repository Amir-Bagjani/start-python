HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="margin:0;padding:0;background:#f4f4f4;font-family:Arial,sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4;padding:40px 0;">
        <tr>
            <td align="center">
                <table width="600" cellpadding="0" cellspacing="0"
                       style="background:#ffffff;border-radius:10px;padding:40px;">
                    <tr>
                        <td>
                            <h1 style="color:#333333;margin-top:0;">
                                Hi {name}! 👋
                            </h1>

                            <p style="font-size:16px;color:#555555;line-height:1.6;">
                                I hope you're having a wonderful day!
                            </p>

                            <p style="font-size:16px;color:#555555;line-height:1.6;">
                                {message}
                            </p>

                            <p style="font-size:16px;color:#555555;line-height:1.6;">
                                If you have any questions, feel free to reply to this email.
                                I'd be happy to help!
                            </p>

                            <p style="margin-top:40px;">
                                Best regards,<br>
                                <strong>{sender}</strong>
                            </p>
                        </td>
                    </tr>
                </table>

                <p style="color:#999999;font-size:12px;margin-top:20px;">
                    This email was sent automatically. Please do not reply if it is a no-reply address.
                </p>
            </td>
        </tr>
    </table>
</body>
</html>
"""
