# Baykar Case / İHA Kiralama Sistemi

Bu belge, URL örnekleri, testleri çalıştırma yönergeleri ve Docker kullanarak projeyi kurma adımları dahil olmak üzere proje için teknik belgeler sağlar.

# Proje bilgisi

Projeye ilgili sayfaları aşağıdaki endpointlerden takip edebilirsiniz. HTML sayfası döndüren viewlarla 
beraber JsonResponse dönen Django Rest Framework de kullanılmıştır. Veritabanı olarak PostgeSQL kullanılmıştır.

Sayfalardan giden istekler AJAX ile yapılımıştır. Kullanılan datatable.js ile oluşturulan tablolardaki; <br>
- arama
- sıralama
- sayfalama

işlemleri server side yapılıp veriler template'dan ajax ile çekilip rest frameworkten gelmektedir.

Aşağıdaki sayfalar templateview olup içerisinde ajax kullanılmıştır.

- `/accounts/login` giriş
- `/accounts/register` kayıt olma
- `/` dashboard index ve "kiraladığım ihalar" sayfası (sadece oturumdaki kullanıcının kayıtları çekilir)
- `/all-rents`  tüm drone kiralama kayıtları sayfası (sadece admin kullanıcı erişebilir)
- `/new-drone-rent` yeni drone kiralama sayfası. bu sayfada daha önceden kiralanan dronelarla tarih çakışması olmaması için kontrol eklenmiştir
- `/update-drone/<int:pk>` drone kiralama güncelleme. sadece kiralayan kullanıcı ve admin yetkisine sahip kullanıcı bu güncellemeyi yapabilir

Aşağıdaki sayfalar APIView olup Rest Framework kullanılmıştır.
- `/drones/my-rented-drones` oturumdaki kullanıcının drone kiralama kayıtları
- `/drones/all-rented-drones` tüm drone kiralama kayıtları (sadece admin erişebilir)
- `/drones/<int:pk>/` [DELETE] ilgili drone'u sil (sadece admin ve sahibi olan kullanıcı erişebilir)


# Projeyi ayağa kaldırmak

### Proje ayağa kaldırma işleminden sonra admin panelinden drone eklenmelidir. 


## Docker ile
   ```shell
 docker-compose up
 ```

## Manuel

Manuel kullanımda settings.py içerisinde yorum satırına alınmış sqlite yapılandırması seçilmeli. PostgreSQL docker kullanırken seçilmeli.

1. Gereklilikleri yükleme
     ```shell
     pip install -r requirements.txt 
     ``` 
2. Migrate işlemi
    ```shell
     python manage.py migrate
     ``` 
3. Projeyi başlatma
    ```shell
     python manage.py runserver
      ```

### Testler:
   ```shell
   python manage.py test
```

### Admin Kullanıcı Oluşturma:
   ```shell
   python manage.py createsuperuser
```


