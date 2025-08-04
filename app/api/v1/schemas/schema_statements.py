from collections import defaultdict
from datetime import date
from typing import Dict
from pydantic import RootModel

class KeyFactorData(RootModel):
    root: Dict[date, float]

    def model_dump(self, **kwargs):
        return {
            k.isoformat(): v for k, v in self.root.items()
        }

class StatementTypeSchema(RootModel):
    root: Dict[str, KeyFactorData]

    @classmethod
    def from_statement(cls, statement):
        nested_data = defaultdict(lambda: defaultdict(dict))
        for label in statement:
            nested_data[label.key_factor][label.date] = float(label.value)
        
        root = {
            key_factor: KeyFactorData(
                root=dates
            )
            for key_factor, dates in nested_data.items()
        }
        
        return cls(root=root)

    def model_dump(self, **kwargs):
        return {
            k: v.model_dump(**kwargs) for k, v in self.root.items()
        }

# hardly use for production live.
class CompanyFactsSchema(RootModel):
    root: Dict[str, StatementTypeSchema]

    @classmethod
    def from_facts(cls, facts):
        nested_data = defaultdict(lambda: defaultdict(dict))
        for fact in facts:
            nested_data[fact.statement_type][fact.key_factor][fact.date] = float(fact.value)

        root = {
            statement_type: StatementTypeSchema(
                root={
                    key_factor: KeyFactorData(root=dates)
                    for key_factor, dates in key_factors.items()
                }
            )
            for statement_type, key_factors in nested_data.items()
        }

        return cls(root=root)

    def model_dump(self, **kwargs):
        return {
            k: v.model_dump(**kwargs) for k, v in self.root.items()
        }