
import unittest
import apache_log_parser
import datetime

class ApacheLogParserTestCase(unittest.TestCase):
    def test_simple(self):
        format_string = "%h <<%P>> %t %Dus \"%r\" %>s %b  \"%{Referer}i\" \"%{User-Agent}i\" %l %u"
        parser = apache_log_parser.make_parser(format_string)
        sample = '127.0.0.1 <<6113>> [16/Aug/2013:15:45:34 +0000] 1966093us "GET / HTTP/1.1" 200 3478  "https://example.com/" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)" - -'
        log_data = parser(sample)
        self.assertNotEqual(log_data, None)
        self.assertEqual(log_data['status'], '200')
        self.assertEqual(log_data['pid'], '6113')
        self.assertEqual(log_data['request_first_line'], 'GET / HTTP/1.1')
        self.assertEqual(log_data['request_method'], 'GET')
        self.assertEqual(log_data['request_url'], '/')
        self.assertEqual(log_data['request_header_referer'], 'https://example.com/')

        self.assertEqual(log_data['request_header_user_agent'], 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.18)')

        self.assertEqual(log_data['request_header_user_agent__os__family'], 'Linux')

        self.assertEqual(apache_log_parser.get_fieldnames(format_string), ('remote_host', 'pid', 'time_received', 'time_us', 'request_first_line', 'status', 'response_bytes_clf', 'request_header_referer', 'request_header_user_agent', 'remote_logname', 'remote_user'))

    def test_pr8(self):
        parser = apache_log_parser.make_parser('%h %{remote}p %v %{local}p %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %P %D %{number}n %{SSL_PROTOCOL}x %{SSL_CIPHER}x %k %{UNIQUE_ID}e ')
        data = parser('127.0.0.1 50153 mysite.co.uk 443 [28/Nov/2014:10:03:40 +0000] "GET /mypage/this/that?stuff=all HTTP/1.1" 200 5129 "-" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36" 18572 363701 0 TLSv1.01 MY-CYPHER 0 VHhIfKwQGCMAAEiMUIAAAAF ')
        self.assertEqual(data, {
            'status': '200', 'extension_ssl_protocol': 'TLSv1.01', 'request_header_user_agent__browser__family': 'Chrome',
            'time_us': '363701', 'num_keepalives': '0', 'request_first_line': 'GET /mypage/this/that?stuff=all HTTP/1.1',
            'pid': '18572', 'response_bytes_clf': '5129', 'request_header_user_agent__os__family': u'Windows 7',
            'request_url': '/mypage/this/that?stuff=all', 'request_http_ver': '1.1',
            'request_header_referer': '-', 'server_name': 'mysite.co.uk', 'request_header_user_agent__is_mobile': False,
            'request_header_user_agent__browser__version_string': '37.0.2062',
            'request_header_user_agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36',
            'note_number': '0', 'request_header_user_agent__os__version_string': '',
            'server_port_local': '443', 'request_method': 'GET',
            'time_received_datetimeobj': datetime.datetime(2014, 11, 28, 10, 3, 40),
            'server_port_remote': '50153', 'env_unique_id': 'VHhIfKwQGCMAAEiMUIAAAAF',
            'time_received_isoformat': '2014-11-28T10:03:40', 'remote_host': '127.0.0.1',
            'extension_ssl_cipher': 'MY-CYPHER', 'time_received': '[28/Nov/2014:10:03:40 +0000]'})

        parser = apache_log_parser.make_parser('%A %V %p %P %a \"%r\" \"%{main_call}n\" %{some_time}t %b %>s %D %{UNIQUE_ID}e ')
        data = parser('127.0.0.1 othersite 80 25572 192.168.1.100 "GET /Class/method/ HTTP/1.1" "-" 20141128155031 2266 200 10991 VHiZx6wQGCMAAEiBE8kAAAAA:VHiZx6wQGiMAAGPkBnMAAAAH:VHiZx6wQGiMAAGPkBnMAAAAH ')
        self.assertEqual(data, {
            'status': '200', 'note_main_call': '-', 'time_some_time': '20141128155031',
            'time_us': '10991', 'request_http_ver': '1.1', 'local_ip': '127.0.0.1',
            'pid': '25572', 'request_first_line': 'GET /Class/method/ HTTP/1.1', 'request_method': 'GET',
            'server_port': '80', 'response_bytes_clf': '2266', 'server_name2': 'othersite',
            'request_url': '/Class/method/',
            'env_unique_id': 'VHiZx6wQGCMAAEiBE8kAAAAA:VHiZx6wQGiMAAGPkBnMAAAAH:VHiZx6wQGiMAAGPkBnMAAAAH',
            'remote_ip': '192.168.1.100'})

if __name__ == '__main__':
    unittest.main()
