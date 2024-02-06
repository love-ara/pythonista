import pytest
from phone_book import PhoneBook

@pytest.fixture
def phone_book():
    return PhoneBook()

def test_add_contact(phone_book):
    result = phone_book.add_contact("Ara", "081224595406")
    assert "Contact 'ARA' added successfully." in result

def test_that_a_contact_exist(phone_book):
    phone_book.add_contact("Ara", "081224595406")
    check = phone_book.search_contact("Ara")
    assert "Ara" in check
    assert "081224595406" in check

def test_that_a_contact_does_not_exist(phone_book):
    check = phone_book.search_contact("Ayo")
    assert "Contact 'Ayo' not found in the phonebook." in check

def test_edit_contact(phone_book):
    phone_book.add_contact("Ara", "090283236783")
    edit = phone_book.edit_contact("Ara", "Ayo", "090283236783", "0702973327")
    assert "Contact 'Ara' edited successfully." in edit

def test_delete_contact(phone_book):
    phone_book.add_contact("Ara", "081224595406")
    delete = phone_book.delete_contact("Ara", "081224595406")
    assert "Contact 'ara' deleted successfully." in delete
    assert not phone_book.get_contact()
