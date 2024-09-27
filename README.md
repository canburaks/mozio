# mozio app task

## Quick Validation

### Access Django admin
Go to [https://mozio.tunn.dev/admin](https://mozio.tunn.dev/admin) and login to the dashboard using the credentials given below
```
username:admin password=mozio2024
```

### Make API calls against the server

Go to [https://mozio.tunn.dev/swagger](https://mozio.tunn.dev/swagger) to see Swagger documentation for API endpoints.

In order to get service areas for a given `lng` and `lat`,
1. Find `search_service_areas` endpoint.
2. Click `Try it now` button.
3. Use `30.792120` for `lng` and `36.906433` for `lat` parameters.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "id": "b9ab6d90-3673-455c-a790-9f50c2d4ae22",
      "type": "Feature",
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [
                30.87542795183588,
                37.07288902451088
              ],
              [
                31.26405885622164,
                37.06132920603127
              ],
              [
                31.271783879807774,
                36.82917790534592
              ],
              [
                30.663932156182476,
                36.88627496405578
              ],
              [
                30.709065186399425,
                37.143955833717925
              ],
              [
                30.87542795183588,
                37.07288902451088
              ]
            ]
          ],
          [
            [
              [
                31.316596871490614,
                37.00002185937059
              ],
              [
                31.393548335808106,
                36.84774977896022
              ],
              [
                31.802315416037626,
                36.99951172356609
              ],
              [
                31.414239061565354,
                37.26573549540633
              ],
              [
                31.177861296906475,
                37.2371730047034
              ],
              [
                31.403254941414566,
                37.07044772641158
              ],
              [
                31.316596871490614,
                37.00002185937059
              ]
            ]
          ]
        ]
      },
      "properties": {
        "name": "GreaterServiceAreaOfFirstProvider",
        "price": 0,
        "provider": {
          "id": "089a40dd-48c0-4c1c-8d12-b68ef2a2a89e",
          "created": "2024-09-26T15:14:54.971913Z",
          "modified": "2024-09-26T15:14:54.971960Z",
          "name": "First Provider",
          "email": "firstprovider@tester.ninja",
          "phone_number": null,
          "language": "EN",
          "currency": "USD"
        }
      }
    }
  ]
}
```


## Design Decisions
- I used Postgres as a database because of its documentation and community posts, especially for the widely known `postgis` extension.
- I used `MultiPolygonField` rather than `PolygonField` for the `ServiceArea' model's geometry field. I assume that any service area may not be a continuous region and may consist of more than one independent but closer proximity.

