import Reaml from 'realm';

class KeyPair extends Realm.Object {

    public private_key!: string;
    public public_key!: string;

    static schema: Realm.ObjectSchema = {
        name: 'KeyPair',
        properties: {
            private_key: 'string',
            public_key: 'string',
        },
    };
}
