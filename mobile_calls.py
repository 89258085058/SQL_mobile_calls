from mobile_calls_query import MobileCallsQuery


class MobileCall():

    def users_operators(self):
        MobileCallsQuery.create_table()

        MobileCallsQuery.insert_users(('User', 500))
        MobileCallsQuery.insert_operators((1, 2, 3))

    def monthly_write_off(self):
        MobileCallsQuery.mouth_call()


mc = MobileCall()
mc.users_operators()
mc.monthly_write_off()
