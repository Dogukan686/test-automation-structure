Feature: Kullanıcı Girişi ve Ürün Sepete Ekleme

  Scenario: Kullanıcı cep telefonu arar, filtre uygular ve ürünü sepete ekler
    Given kullanıcı e-ticaret sitesine gider
    And kullanıcı giriş yapar
    When kullanıcı "cep telefonu" araması yapar
    And fiyat aralığını 15000 - 20000 TL olarak filtreler
    And en alt sıradaki ürünü seçip detayına gider
    And en düşük puanlı satıcının ürününü sepete ekler
    Then ürünün sepete doğru şekilde eklendiği kontrol edilir
