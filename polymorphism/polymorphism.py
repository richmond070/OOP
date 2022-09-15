# polymorphism is the ability of a message to be displayed in more than one form
# in polymorphism you can create methods in the child class that have the same name as methods in the parent class

class Africa:
    def country(self):
        print("Africa has 52 countries.")

    def state(self):
        print("I love Africa")


class nigeria(Africa):
    def state(self):
        print("Nigeria is a country in Africa")


class ghana(Africa):
    def state(self):
        print('Ghana is a country in Africa')


class togo(Africa):
    def state(self):
        print('Togo is a country in Africa')


con_africa = Africa()
con_nig = nigeria()
con_gh = ghana()
con_tg = togo()

con_africa.country()
con_africa.state()

con_nig.country()
con_nig.state()

con_gh.country()
con_gh.state()

con_tg.country()
con_tg.state()


# polymorphism can also take place in creating loops



