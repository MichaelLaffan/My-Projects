# main function

descriptions = [('''Our first location here is the Murray Student Center. This location   
serves as the center point of the college. It brings together all
the members of Marist College. It provides various student services
and serves as a place where students can meet and organize events.
Some of these services include dining services, student lounge,
the campus post office, and the campus bookstore.'''), ('''Our next location here is Donnelly Hall. This location mainly houses
our technology services and other offices that are available to
our students here on campus. Some of these services include
Financial services, the Help Desk, Advising and Academic Services
and the Computer Lab.'''), ('''Our next location here is the Hancock Center. This location is
for our School of Computer Science and Mathematics. However, it also
houses our Study Abroad offices, which manages our programs for students
who want to go and study in another country, such as our campus in
Florence, Italy. It also houses our Investment Center and Trading Room
and our Center for Teaching Excellence.'''), ('''Our next location here is the McCann Center. This location is mostly
known to be our sports center here on campus. It houses our Athletic
Department, our fitness center, our Center for Sports Medicine, and
other sports services. It also houses our Admissions Visitor Center
for people who come to visit our campus.'''), ('''Our next location here is the Cannavino Library. This location serves
as our main library here on campus. It also serves as a place where
students can catch up on their work and study without any distractions.
It also houses our Center for Career Services, Center for Multicultural
Affairs, and our Digital Education services.'''), ('''Our next location here is the Chapel. The Chapel serves as an
Inter-Faith Prayer room, where anyone can come in for quiet
prayer from 7 am to 10 pm. It also provides Mass services
Monday through Thursday at 12:15 pm and on Sundays at both
12 pm and 6:30 pm.'''), ('''Our next location here is McCormick Hall. This location serves as a
residence hall for our upperclassmen. Unlike the freshman residence
halls we have here on campus, residents of this hall are responsible
for their own cooking and cleaning of their apartment. This location
also serves as one of our dining locations here on campus, also
known as North End Dining.'''), ('''Our next location is the Steel Plant Studios and Gallery, commonly
known as the Steel Plant. This building mainly houses our fashion
and design programs that we have available here on campus. It also
houses our Art Gallery and our Digital Media and Fine Arts programs
here as well.'''), ('''Our next location here is the Science and Allied Health Building.
This building mainly houses our science and medical field programs.
It also houses our School of Science and our labratories such as the
Cognitive Computing Lab and Gross Anatomy Lab. Anyone interested in
the medical field will likely take most of their classes here.'''), ('''Our last location that I will be showing you here at Marist College
is the Dyson Center. This building houses our School of Management
and School of Social and Behavioral Sciences. It also houses our
Teacher Education Program for any students that wish to pursue a
career in teaching and it also has a coffee shop.''')]

details = [('''The dorms that are adjacent to the Student Center are Champangat Hall
and Midrise Hall. Champagnat is a freshman residence consisting of nine floors and has
rooms consisting of doubles. Midrise hall is a suite style residence hall and houses
freshman, sophomore and transfer students.'''), ('''The other services we have available here are the Accomodations
and Accessibility, the Registrar office, Safety and Security, ResNet, and
Business and Financial Affairs.'''), ('''Our Study Abroad locations include Japan, Italy, Greece, France,
Australia, Spain, and China.'''), ('''The primary sports that are available here at Marist are
basketball, soccer, volleyball, flag football, and softball.'''), ('''The library has a tool called Fox Hunt that allows you to
look for any book that is available in the library. It also allows you to
access any workshop that gives you information about other services we have
here on campus such as counseling.'''), ('''The Chapel hosts spirit groups for men, women, and different
faiths. Some of the topics discussed in these spirit groups are personal
identity, transitions into college, and sprituality.'''), ('''Some of our food options that are available at North End
Dining are cheese quesadillas, cheeseburgers, crispy chicken sandwich,
and cheese and pepperoni pizza.'''), ('''The Art Gallery is a 3200 square foot art exhibition space
and retains the industrial look of the former steel plant. It focuses on
contemporary regional artists working in fine arts media.'''), ('''Our Physician Assistant program is a 24 month, full time program
designed to prepare our students for clinical practice. Students learn how to
care in a variety of settings such as in the operating and emergency room.'''), ('''Some of our programs of study for our education majors is the
Adolescence Education program, Special Education program, and M.A.s in Education
Psychology and Initial Teaching Certification.''')]

locations = 0
count = 0
def main():
    #Title and Introduction
    global locations
    global count
    i1 = "Marist Virtual Tour" 
    i2 = "Hello everyone! Welcome to Marist College. I'll be your tour guide as I show you some of our locations here on campus. Enjoy the tour."
    i3 = "Press the enter key to begin the tour: "
    print(i1)
    print(i2)
    print(input(i3))
    
    #Location 1 - Student Center
    print()
    s1 = "Murray Student Center"
    s2 = "Press the enter key for information on the dorms next to the Student Center: "
    s3 = "Press the enter key to go to the next location: "
    print(s1)
    print(descriptions[locations])
    print(input(s2))
    print(details[locations])
    print(input(s3))
    count = count + 1
    locations = locations + 1
    
    #Location 2 - Donnelly Hall
    print()
    d1 = "Donnelly Hall"
    d2 = "Press the enter key for a list of the other services: "
    d3 = "Press the enter key to go to the next location: "
    print(d1)
    print(descriptions[locations])
    print(input(d2))
    print(details[locations])
    print(input(d3))
    count = count + 1
    locations = locations + 1
    
    #Location 3 - Hancock Center
    print()
    h1 = "Hancock Center"
    h2 = "Press the enter key for a list of some of our Study Abroad locations: "
    h3 = "Press the enter key to go to the next location: "
    print(h1)
    print(descriptions[locations])
    print(input(h2))
    print(details[locations])
    print(input(h3))
    count = count + 1
    locations = locations + 1
    
    #Location 4 - McCann Center
    print()
    m1 = "McCann Center"
    m2 = "Press the enter key for a list sports we have here: "
    m3 = "Press the enter key to go to the next location: "
    print(m1)
    print(descriptions[locations])
    print(input(m2))
    print(details[locations])
    print(input(m3))
    count = count + 1
    locations = locations + 1
    
    #Location #5 - Cannavino Library
    print()
    c1 = "Cannavino Library"
    c2 = "Press the enter key for information on the digital library: "
    c3 = "Press the enter key to go to the next location: "
    print(c1)
    print(descriptions[locations])
    print(input(c2))
    print(details[locations])
    print(input(c3))
    count = count + 1
    locations = locations + 1
    
    #Location #6 - The Chapel
    print()
    ch1 = "The Chapel"
    ch2 = "Press the enter key for information on our spirit groups: "
    ch3 = "Press the enter key to go to the next location: "
    print(ch1)
    print(descriptions[locations])
    print(input(ch2))
    print(details[locations])
    print(input(ch3))
    count = count + 1
    locations = locations + 1
    
    #Location #7 - McCormick Hall
    print()
    mc1 = "McCormick Hall"
    mc2 = "Press the enter key for a list of our food options: "
    mc3 = "Press the enter key to go to the next location: "
    print(mc1)
    print(descriptions[locations])
    print(input(mc2))
    print(details[locations])
    print(input(mc3))
    count = count + 1
    locations = locations + 1
    
    #Location 8 - Steel Plant Studios and Gallery
    print()
    sp1 = "Steel Plant Studios and Gallery"
    sp2 = "Press the enter key for more information on the Art Gallery: "
    sp3 = "Press the enter key to go to the next location: "
    print(sp1)
    print(descriptions[locations])
    print(input(sp2))
    print(details[locations])
    print(input(sp3))
    count = count + 1
    locations = locations + 1
    
    #Location 9 - Science and Allied Health Building
    print()
    sc1 = "Science and Allied Health Building"
    sc2 = "Press the enter key for information on our Physician Assist Program: "
    sc3 = "Press the enter key to go to the last location: "
    print(sc1)
    print(descriptions[locations])
    print(input(sc2))
    print(details[locations])
    print(input(sc3))
    count = count + 1
    locations = locations + 1
    
    #Location 10 - Dyson Center
    print()
    dy1 = "Dyson Center"
    dy2 = "Press the enter key for a list of our teacher education programs: "
    dy3 = "Press the enter key to end the tour: "
    print(dy1)
    print(descriptions[locations])
    print(input(dy2))
    print(details[locations])
    print(input(dy3))
    count = count + 1
    
    #Closing
    print()
    print("You have visited", count, "locations.")
    cl = ('''Thank you everyone for visiting Marist College. I hope you enjoyed
the tour and consider applying to Marist College. Goodbye!''')
    print(cl)


main()
