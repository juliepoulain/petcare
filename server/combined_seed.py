from config import db, app
from random import randint, choice as rc
from datetime import date, time, datetime
from models import Owner, Pet, Sitter, Visit

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")

with app.app_context():

    print("Deleting visits...")
    Visit.query.delete()
    print("Deleting sitters...")
    Sitter.query.delete()
    print("Deleting pets...")
    Pet.query.delete()
    print("Deleting owners...")
    Owner.query.delete()
    print("Creating owners...")
    julie = Owner(name="Julie", address='julieaddress', email="julieemail@gmail.com", phone=9785510848)
    billy = Owner(name="Billy", address="billyaddress", email="billyemail", phone=1111111112)
    bia = Owner(name="Bia", address="biaaddress2", email="biaemail", phone=1111111113)
    owners = [julie, billy, bia]
    db.session.add_all(owners)
    db.session.commit()

    print("Adding pets...")
    garfield = Pet(name="Garfield", image="https://images.pexels.com/photos/4587955/pexels-photo-4587955.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", animal="cat", age=3, temperament="lazy", owner_id=julie.id, breed="shorthair")
    rose = Pet(name="Rose", image="https://img.freepik.com/free-photo/close-up-portrait-beautiful-cat_23-2149214419.jpg", animal="cat", age=1, temperament="not friendly", owner_id=billy.id)
    buddy = Pet(name="Buddy", image="https://image.shutterstock.com/image-photo/happy-puppy-dog-smiling-on-260nw-1799966587.jpg", animal="dog", age=11, temperament="friendly", owner_id=billy.id)
    olivia = Pet(name="Olivia", image="https://i.imgur.com/HhvboVU.jpeg", animal="cat", age=4, temperament="avoidant", owner_id=julie.id, breed="shorthair")
    pets=[garfield, rose, buddy, olivia]
    db.session.add_all(pets)
    db.session.commit()

    print("Creating sitters...")
    sitters = [
        Sitter(
            name="Hannah",
            bio="Cats, dogs, and coffee are all I need in life!",
            experience=7,
            image="https://images.nightcafe.studio/jobs/6sLDmT6whBds1MnmQf6y/6sLDmT6whBds1MnmQf6y--1--5hp52_2x.jpg?tr=w-1200,c-at_max",
            address="12 Crystal Lake, Wantabe, NJ 07050",
            phone=1111111111,
            email="hannah@example.com"
        ),
        Sitter(
            name="Kelly",
            bio="Responsible and timely!",
            experience=10,
            image="https://static1.srcdn.com/wordpress/wp-content/uploads/2016/10/Nightmare-on-Elm-Street-6.jpg",
            address="1428 Elm Street, Springwood, OH 45459",
            phone=1111111111,
            email="kelly@example.com"
        ),
        Sitter(
            name="Michael",
            bio="Pet lover",
            experience=8,
            image="https://coleandmarmalade.com/wp-content/uploads/2022/03/Michael-Meowers-1.jpg",
            address="45 Lampkin Lane, Haddonfield, IL 60120",
            phone=1111111111,
            email="michael@example.com"
        ),
        Sitter(
            name="Terri",
            bio="Great with pets, especially if they like to play",
            experience=5,
            image="https://static1.srcdn.com/wordpress/wp-content/uploads/2021/10/Brad-Dourif-as-Chucky-with-Binx-the-Cat-in-Chucky-Episode-1.jpg",
            address="123 Good Guys St, Hackensack, NJ 07601",
            phone=1111111111,
            email="Terri@example.com"
        ),
        Sitter(
            name="Allison",
            bio="I'll take care of your pets like they're my own!",
            experience=6,
            image="https://m.media-amazon.com/images/M/MV5BMWZiYmM3MzItYzFiOC00N2VmLWEwOWQtZTYzYjFmNjZlMWRlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNzAzMDEzNTI@._V1_.jpg",
            address="12 Old Highway, Fairvale, CA 93922",
            phone=1111111111,
            email="ally@example.com"
        ),
        Sitter(
            name="Penny",
            bio="I love all animals!!",
            experience=9,
            image="https://photos.costume-works.com/full/pennywise_and_his_dog-31298-1.jpg",
            address="29 Neibolt Street, Derry, ME 04401",
            phone=1111111111,
            email="penny@example.com"
        )
    ]
    for sitter in sitters:
        db.session.add(sitter)
    db.session.commit()

    print("Creating visits...")
    visitA = Visit(visit_notes="Garfield was very sweet today. He ate all his food and I watched him drink some water. We played fetch for a while and cuddled while watching Bridgerton. A great visit!", sitter_id=sitters[0].id, pet_id=garfield.id, owner_id=julie.id, date=date(2024, 1, 2), check_in_time=time(14, 27))
    visitB = Visit(visit_notes="Garfield was aloof today. I guess we're not friends anymore. I am sad.", sitter_id=sitters[0].id, pet_id=garfield.id, owner_id=julie.id, date=date(2024, 2, 1), check_in_time=time(12, 12))
    visitC = Visit(visit_notes="Rose was a good girl!", sitter_id=sitters[1].id, pet_id=rose.id, owner_id=billy.id, date=date(2024, 5, 27), check_in_time=time(15, 32))
    visitD = Visit(visit_notes="Buddy was very bad today. I would like an added tip for the inconvenience.", sitter_id=sitters[2].id, pet_id=buddy.id, owner_id=billy.id, date=date(2024, 6, 15), check_in_time=time(10, 15))
    visitE = Visit(visit_notes="Nothing to report.", sitter_id=sitters[3].id, pet_id=rose.id, owner_id=billy.id, date=date(2024, 8, 10), check_in_time=time(9, 45))
    visitF = Visit(visit_notes="Nothing to report.", sitter_id=sitters[4].id, pet_id=buddy.id, owner_id=billy.id, date=date(2024, 9, 20), check_in_time=time(11, 30))
    visitG = Visit(visit_notes="I adore garfield!", sitter_id=sitters[5].id, pet_id=garfield.id, owner_id=julie.id, date=date(2024, 10, 5), check_in_time=time(14, 0))
    visitH = Visit(visit_notes="Olivia is so cute!!!! She hid from me at first but then came out for cuddles", sitter_id=sitters[2].id, pet_id=olivia.id, owner_id=julie.id, date=date(2024, 10, 5), check_in_time=time(14, 0))
    visits = [visitA, visitB, visitC, visitD, visitE, visitF, visitG, visitH]
    db.session.add_all(visits)
    db.session.commit()

    print("Seeding done!")

    

    
    