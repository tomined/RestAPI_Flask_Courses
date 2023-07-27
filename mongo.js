// lista baz

show dbs

// utworz baze i przełącz do niej
use courses

// umieść nowy dokument w kolekcji

db.entries.insertOne({
    name:"Junior Front End",
    category:"Programing",
    price:4500,
    city:"warszawa",
    hours:70
})


// pokaż wzystkie dokumenty w kolekcji

db.entries.find({})

// pokaż wszystkie w krakowie

db.entries.find({city:"Kraków"})

// dokument zaupełnie inny od reszty z kolekcji courses
db.entries.insertOne({
    firstname: "Jan",
    age:30
})


// usóń dokument
db.entries.deleteOne({_id: ObjectId("64b95d77c92538d5aad9bc9e")})


// zmoiana nazwy kolecki z etries na nowaNazwa
db.etires.renameCollection("nowaNazwa")


//kopiowanie danych z jednej kolekcji do drgiej
db.new.aggregate( [
    { $project: { _id: 0 } },
    { $merge : { into : "entries" } }
 ] )